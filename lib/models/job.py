from models.initializer import CURSOR, CONN
from models.employee import Employee

class Job:
    all = {}

    def __init__(self, title, description, employer_id=None):
        self.job_id = None
        self.title = title
        self.description = description
        self.employer_id = employer_id

    def __repr__(self):
        return f"<Job {self.job_id}: {self.title}>"
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value) > 5:
            self._title = value
        else:
            raise ValueError("Title must be a string with at least 5 characters")

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if isinstance(value, str) and len(value) > 50:
            self._description = value
        else:
            raise ValueError("Description should be a string with more than 50 characters")   

    @property
    def employer_id(self):
        return self._employer_id
    
    @employer_id.setter
    def employer_id(self, value):
        if isinstance(value, int):
            self._employer_id = value
        else:
            raise ValueError("Employer ID must be an integer")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS jobs (
                job_id INTEGER PRIMARY KEY,
                title TEXT,
                description TEXT,
                employer_id INTEGER,
                FOREIGN KEY(employer_id) REFERENCES employers(employer_id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS jobs;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO jobs (title, description, employer_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.title, self.description, self.employer_id))
        CONN.commit()
        self.job_id = CURSOR.lastrowid
        type(self).all[self.job_id] = self

    def update(self):
        sql = """
            UPDATE jobs
            SET title = ?, description = ?
            WHERE job_id = ?
        """
        CURSOR.execute(sql, (self.title, self.description, self.job_id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM jobs
            WHERE job_id = ?
        """
        CURSOR.execute(sql, (self.job_id,))
        CONN.commit()
        del type(self).all[self.job_id]
        self.job_id = None

    @classmethod
    def create(cls, title, description, employer_id=None):
        job = cls(title, description, employer_id)
        job.save()
        return job

    @classmethod
    def instance_from_db(cls, row):
        job = cls.all.get(row[0])
        if job:
            job.title = row[1]
            job.description = row[2]
            job.employer_id = row[3]
        else:
            job = cls(row[1], row[2], row[3])
            job.job_id = row[0]
            cls.all[job.job_id] = job
        return job

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM jobs"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, job_id):
        sql = "SELECT * FROM jobs WHERE job_id = ?"
        row = CURSOR.execute(sql, (job_id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_employer(cls, employer_id):
        sql = "SELECT * FROM jobs WHERE employer_id = ?"
        rows = CURSOR.execute(sql, (employer_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_employee_job_info(cls, job_id):
        sql = """
            SELECT employees.name, jobs.title, jobs.description
            FROM employees
            JOIN employee_jobs ON employees.employee_id = employee_jobs.employee_id
            JOIN jobs ON employee_jobs.job_id = jobs.job_id
            WHERE jobs.job_id = ?
        """
        rows = CURSOR.execute(sql, (job_id)).fetchall()
        return [(row[0], row[1], row[2]) for row in rows]

