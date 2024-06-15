from models.initializer import CURSOR, CONN

class Employer_Job:
    all = {}

    def __init__(self, employer_id, job_id):
        self.employer_id = employer_id
        self.job_id = job_id
    
    def __repr__(self):
        return f"<Employer_Job: Employer ID {self.employer_id}, Job ID {self.job_id}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS employers_jobs (
                employer_id INTEGER,
                job_id INTEGER,
                FOREIGN KEY(employer_id) REFERENCES employers(employer_id),
                FOREIGN KEY(job_id) REFERENCES jobs(job_id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS employers_jobs;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO employers_jobs (employer_id, job_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.employer_id, self.job_id))
        CONN.commit()
        type(self).all[(self.employer_id, self.job_id)] = self

    @classmethod
    def find_jobs_by_employer(cls, employer_id):
        """Find all jobs associated with an employer."""
        sql = """
            SELECT jobs.job_id, jobs.title, jobs.description
            FROM jobs
            JOIN employers_jobs ON jobs.job_id = employers_jobs.job_id
            WHERE employers_jobs.employer_id = ?
        """
        rows = CURSOR.execute(sql, (employer_id,)).fetchall()
        return [(row[0], row[1], row[2]) for row in rows]

    @classmethod
    def find_employers_by_job(cls, job_id):
        """Find all employers associated with a job."""
        sql = """
            SELECT employers.employer_id, employers.name, employers.company_name
            FROM employers
            JOIN employers_jobs ON employers.employer_id = employers_jobs.employer_id
            WHERE employers_jobs.job_id = ?
        """
        rows = CURSOR.execute(sql, (job_id,)).fetchall()
        return [(row[0], row[1], row[2]) for row in rows]
