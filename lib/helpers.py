from models.job import Job
from models.employee import Employee
from models.employee_job import Employee_Job

def list_jobs():
    jobs = Job.get_all()
    for job in jobs:
        print(job)

def find_job_by_id():
    job_id = input("Enter the job's ID: ")
    job = Job.find_by_id(job_id)
    print(job) if job else print(f'Job {job_id} not found')

def create_job():
    title = input("Enter the job's title: ")
    description = input("Enter the job's description: ")
    employer_id = input("Enter the employer's ID: ")
    job = Job(title, description, employer_id)
    job.save()
    print(f'Job {job.job_id} created successfully')

def update_job():
    job_id = input("Enter the job's ID to update: ")
    job = Job.find_by_id(job_id)
    if job:
        title = input("Enter the new title (leave empty to keep current): ")
        description = input("Enter the new description (leave empty to keep current): ")
        
        if title:
            job.title = title
        if description:
            job.description = description
        job.update_job()
        print(f'Job {job_id} updated successfully')
    else:
        print(f'Job {job_id} not found')

def delete_job():
    job_id = input("Enter the job's ID to delete: ")
    job = Job.find_by_id(job_id)
    if job:
        job.delete()
        print(f'Job {job_id} deleted successfully')
    else:
        print(f'Job {job_id} not found')

def list_jobs_by_employer():
    employer_id = input("Enter the employer's ID to list jobs: ")
    jobs = Job.find_by_employer(employer_id)
    for job in jobs:
        print(job)

def list_employees_for_job():
    job_id = input("Enter the job's ID to list employees: ")
    employees = Employee_Job.get_employees_for_job(job_id)
    for employee_id, name in employees:
        print(f"Employee ID: {employee_id}, Name: {name}")

def list_jobs_for_employee():
    employee_id = input("Enter the employee's ID to list jobs: ")
    jobs = Employee_Job.get_jobs_for_employee(employee_id)
    for job_id, title, description, employer_name in jobs:
        print(f"Job ID: {job_id}, Title: {title}, Description: {description}, Employer: {employer_name}")

def assign_employee_to_job():
    employee_id = input("Enter the employee's ID: ")
    job_id = input("Enter the job's ID: ")
    Employee_Job.save(employee_id, job_id)
    print(f'Employee {employee_id} assigned to job {job_id}')

def unassign_employee_from_job():
    employee_id = input("Enter the employee's ID: ")
    job_id = input("Enter the job's ID: ")
    Employee_Job.delete(employee_id, job_id)
    print(f'Employee {employee_id} unassigned from job {job_id}')
