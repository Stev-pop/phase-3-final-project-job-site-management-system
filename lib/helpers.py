from models.job import Job
from models.employer import Employer

def exit_program():
    print("Goodbye!")
    exit()

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

def list_employers():
    employers = Employer.get_all()
    for employer in employers:
        print(employer)

def find_employer_by_id():
    """Find an employer by his/her ID."""
    
    employer_id = input("Enter the employer's ID: ")
    employer = Employer.find_by_id(employer_id)
    print(employer) if employer else print(f'Employer {employer_id} not found')

def create_employer():
    """Create a new employer."""

    name = input("Enter the employer's name: ")
    company_name = input("Enter the employer's company name: ")
    employer = Employer(name, company_name)
    employer.save()
    print(f'Employer {employer.employer_id} created successfully')

def update_employer():
    """Update an employer."""

    employer_id = input("Enter the employer's ID to update: ")
    employer = Employer.find_by_id(employer_id)
    if employer:
        name = input("Enter the new name (leave empty to keep current): ")
        company_name = input("Enter the new company name (leave empty to keep current): ")
        if name:
            employer.name = name
        if company_name:
            employer.company_name = company_name
        employer.update_employer()
        print(f'Employer {employer_id} updated successfully')
    else:
        print(f'Employer {employer_id} not found')

def delete_employer():
    """Delete an employer."""

    employer_id = input("Enter the employer's ID to delete: ")
    employer = Employer.find_by_id(employer_id)
    if employer:
        employer.delete()
        print(f'Employer {employer_id} deleted successfully')
    else:
        print(f'Employer {employer_id} not found')


def find_jobs_with_employer_names_input():
    """Find all jobs with the associated employer name based on user input."""
    
    employer_id = input("Enter the employer's ID to find associated jobs: ")
    jobs = Employer.find_jobs_with_employer_names(employer_id)
    for job in jobs:
        print(job)
        