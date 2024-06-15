from models.initializer import CURSOR, CONN
from models.job import Job

class Employer:
    all = {}

    def __init__(self, name, company_name, employer_id=None):
        self.employer_id = employer_id
        self._name = None
        self._company_name = None
        self.name = name
        self.company_name = company_name

    def __repr__(self):
        return f"<Employer {self.employer_id}: {self.name}, Company: {self.company_name}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        if isinstance(company_name, str) and len(company_name) > 0:
            self._company_name = company_name
        else:
            raise ValueError("Company name must be a non-empty string")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS employers (
                employer_id INTEGER PRIMARY KEY,
                name TEXT,
                company_name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS employers;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO employers (name, company_name)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.company_name))
        CONN.commit()
        self.employer_id = CURSOR.lastrowid
        type(self).all[self.employer_id] = self

    def update_employer(self):
        sql = """
            UPDATE employers
            SET name = ?, company_name = ?
            WHERE employer_id = ?
        """
        CURSOR.execute(sql, (self.name, self.company_name, self.employer_id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM employers
            WHERE employer_id = ?
        """
        CURSOR.execute(sql, (self.employer_id,))
        CONN.commit()
        del type(self).all[self.employer_id]
        self.employer_id = None

    @classmethod
    def instance_from_db(cls, row):
        employer = cls.all.get(row[0])
        if employer:
            employer.name = row[1]
            employer.company_name = row[2]
        else:
            employer = cls(row[1], row[2])
            employer.employer_id = row[0]
            cls.all[employer.employer_id] = employer
        return employer

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM employers"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, employer_id):
        sql = "SELECT * FROM employers WHERE employer_id = ?"
        row = CURSOR.execute(sql, (employer_id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def get_job_count(self):
        sql = """
            SELECT COUNT(*)
            FROM jobs
            WHERE employer_id = ?
        """
        result = CURSOR.execute(sql, (self.employer_id,)).fetchone()
        return result[0] if result else 0

    def get_jobs(self):
        sql = """
            SELECT *
            FROM jobs
            WHERE employer_id = ?
        """
        rows = CURSOR.execute(sql, (self.employer_id,)).fetchall()
        return [Job.instance_from_db(row) for row in rows]

    def create_job(self, title, description):
        job = Job(title, description, self.employer_id)
        job.save()
        return job

    @classmethod
    def find_jobs_by_id(cls, job_id):
        sql = "SELECT * FROM jobs WHERE job_id = ?"
        row = CURSOR.execute(sql, (job_id,)).fetchone()
        return Job.instance_from_db(row) if row else None

    @classmethod
    def find_jobs_with_employer_name(cls):
        sql = """
            SELECT jobs.job_id, jobs.title, jobs.description, employers.name as employer_name
            FROM jobs
            JOIN employers ON jobs.employer_id = employers.employer_id
        """
        rows = CURSOR.execute(sql).fetchall()
        return [(row[0], row[1], row[2], row[3]) for row in rows]

    @classmethod
    def find_jobs_with_employer_names(cls, employer_id):
        sql = """
            SELECT jobs.job_id, jobs.title, jobs.description, employers.name as employer_name
            FROM jobs
            JOIN employers ON jobs.employer_id = employers.employer_id
            WHERE employers.employer_id = ?
        """
        rows = CURSOR.execute(sql, (employer_id,)).fetchall()
        return [(row[0], row[1], row[2], row[3]) for row in rows]
