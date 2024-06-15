from models.initializer import CURSOR, CONN

class Employee_Job:
    all = {}

    def __init__(self, employee_id, job_id):
        self.employee_id = employee_id
        self.job_id = job_id

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS employee_jobs (
                employee_id INTEGER,
                job_id INTEGER,
                PRIMARY KEY (employee_id, job_id),
                FOREIGN KEY(employee_id) REFERENCES employees(employee_id),
                FOREIGN KEY(job_id) REFERENCES jobs(job_id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS employee_jobs;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def save(cls, employee_id, job_id):
        sql = """
            INSERT INTO employee_jobs (employee_id, job_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (employee_id, job_id))
        CONN.commit()

    @classmethod
    def delete(cls, employee_id, job_id):
        sql = """
            DELETE FROM employee_jobs
            WHERE employee_id = ? AND job_id = ?
        """
        CURSOR.execute(sql, (employee_id, job_id))
        CONN.commit()

    @classmethod
    def get_jobs_for_employee(cls, employee_id):
        sql = """
            SELECT jobs.job_id, jobs.title, jobs.description, employers.name as employer_name
            FROM jobs
            JOIN employers ON jobs.employer_id = employers.employer_id
            JOIN employee_jobs ON jobs.job_id = employee_jobs.job_id
            WHERE employee_jobs.employee_id = ?
        """
        rows = CURSOR.execute(sql, (employee_id,)).fetchall()
        return [(row[0], row[1], row[2], row[3]) for row in rows]

    @classmethod
    def get_employees_for_job(cls, job_id):
        sql = """
            SELECT employees.employee_id, employees.name
            FROM employees
            JOIN employee_jobs ON employees.employee_id = employee_jobs.employee_id
            WHERE employee_jobs.job_id = ?
        """
        rows = CURSOR.execute(sql, (job_id,)).fetchall()
        return [(row[0], row[1]) for row in rows]
