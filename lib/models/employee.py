from models.initializer import CURSOR, CONN

class Employee:
    all = {}

    def __init__(self, name, employee_id=None):
        self.employee_id = employee_id
        self.name = name

    def __repr__(self):
        return f"<Employee {self.employee_id}: {self.name}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            ValueError ("Name must be a string with atleast 1 character")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS employees (
                employee_id INTEGER PRIMARY KEY,
                name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS employees;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO employees (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.employee_id = CURSOR.lastrowid
        type(self).all[self.employee_id] = self

    def update_employee(self):
        sql = """
            UPDATE employees
            SET name = ?
            WHERE employee_id = ?
        """
        CURSOR.execute(sql, (self.name, self.employee_id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM employees
            WHERE employee_id = ?
        """
        CURSOR.execute(sql, (self.employee_id,))
        CONN.commit()
        del type(self).all[self.employee_id]
        self.employee_id = None

    @classmethod
    def create(cls, name):
        employee = cls(name)
        employee.save()
        return employee

    @classmethod
    def instance_from_db(cls, row):
        employee = cls.all.get(row[0])
        if employee:
            employee.name = row[1]
        else:
            employee = cls(row[1])
            employee.employee_id = row[0]
            cls.all[employee.employee_id] = employee
        return employee

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM employees"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, employee_id):
        sql = "SELECT * FROM employees WHERE employee_id = ?"
        row = CURSOR.execute(sql, (employee_id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM employees WHERE name = ?"
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def get_jobs(self):
        sql = """
            SELECT jobs.job_id, jobs.title, jobs.description
            FROM jobs
            JOIN employee_jobs ON jobs.job_id = employee_jobs.job_id
            WHERE employee_jobs.employee_id = ?
        """
        rows = CURSOR.execute(sql, (self.employee_id,)).fetchall()
        return [(row[0], row[1], row[2]) for row in rows]

    def assign_to_job(self, job_id):
        sql = """
            INSERT INTO employee_jobs (employee_id, job_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.employee_id, job_id))
        CONN.commit()

    def unassign_from_job(self, job_id):
        sql = """
            DELETE FROM employee_jobs
            WHERE employee_id = ? AND job_id = ?
        """
        CURSOR.execute(sql, (self.employee_id, job_id))
        CONN.commit()

    def get_job_count(self):
        sql = """
            SELECT COUNT(*)
            FROM employee_jobs
            WHERE employee_id = ?
        """
        count = CURSOR.execute(sql, (self.employee_id,)).fetchone()[0]
        return count
