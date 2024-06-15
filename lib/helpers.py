from models.job import Job
from models.employee import Employee
from lib.models.employer import Employee_Job

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
    try:
        job = Job(title, description, employer_id)
        job.save()
        print(f'Job {job.job_id} created successfully')
    except ValueError as e:
        print(e)

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
    if Employee_Job._validate_employee(employee_id) and Employee_Job._validate_job(job_id):
        Employee_Job.save(employee_id, job_id)
        print(f'Employee {employee_id} assigned to job {job_id}')
    else:
        print("Invalid employee_id or job_id")

def unassign_employee_from_job():
    employee_id = input("Enter the employee's ID: ")
    job_id = input("Enter the job's ID: ")
    Employee_Job.delete(employee_id, job_id)
    print(f'Employee {employee_id} unassigned from job {job_id}')
    
def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)

def find_employee_by_id():
    employee_id = input("Enter the employee's ID: ")
    employee = Employee.find_by_id(employee_id)
    print(employee) if employee else print(f'Employee {employee_id} not found')

def create_employee():
    name = input("Enter the employee's name: ")
    try:
        employee = Employee.create(name)
        print(f'Employee {employee.employee_id} created successfully')
    except ValueError as e:
        print(e)

def update_employee():
    employee_id = input("Enter the employee's ID to update: ")
    employee = Employee.find_by_id(employee_id)
    if employee:
        name = input("Enter the new name: ")
        if name:
            employee.name = name
        employee.update_employee()
        print(f'Employee {employee_id} updated successfully')
    else:
        print(f'Employee {employee_id} not found')

def delete_employee():
    employee_id = input("Enter the employee's ID to delete: ")
    employee = Employee.find_by_id(employee_id)
    if employee:
        employee.delete()
        print(f'Employee {employee_id} deleted successfully')
    else:
        print(f'Employee {employee_id} not found')

def employee_job_count():
    employee_id = input("Enter the employee's ID: ")
    employee = Employee.find_by_id(employee_id)
    if employee:
        count = employee.get_job_count()
        print(f'Employee {employee_id} is assigned to {count} jobs')
    else:
        print(f'Employee {employee_id} not found')

def job_info_for_employee():
    job_id = input("Enter the job's ID to get info: ")
    info = Job.find_employee_job_info(job_id)
    if info:
        for employee_name, job_title, job_description in info:
            print(f'Employee: {employee_name}, Job Title: {job_title}, Job Description: {job_description}')
    else:
            print(f'Job {job_id} not found')

# def show_menu():
#     menu = """
#     1. List all jobs
#     2. Find job by ID
#     3. Create a job
#     4. Update a job
#     5. Delete a job
#     6. List jobs by employer
#     7. List employees for a job
#     8. List jobs for an employee
#     9. Assign employee to job
#     10. Unassign employee from job
#     11. List all employees
#     12. Find employee by ID
#     13. Create an employee
#     14. Update an employee
#     15. Delete an employee
#     16. Show job count for employee
#     17. Show job info for employee
#     18. Exit
#     """
#     print(menu)

# def main():
#     while True:
#         show_menu()
#         choice = input("Enter your choice: ")
#         if choice == '1':
#             list_jobs()
#         elif choice == '2':
#             find_job_by_id()
#         elif choice == '3':
#             create_job()
#         elif choice == '4':
#             update_job()
#         elif choice == '5':
#             delete_job()
#         elif choice == '6':
#             list_jobs_by_employer()
#         elif choice == '7':
#             list_employees_for_job()
#         elif choice == '8':
#             list_jobs_for_employee()
#         elif choice == '9':
#             assign_employee_to_job()
#         elif choice == '10':
#             unassign_employee_from_job()
#         elif choice == '11':
#             list_employees()
#         elif choice == '12':
#             find_employee_by_id()
#         elif choice == '13':
#             create_employee()
#         elif choice == '14':
#             update_employee()
#         elif choice == '15':
#             delete_employee()
#         elif choice == '16':
#             employee_job_count()
#         elif choice == '17':
#             job_info_for_employee()
#         elif choice == '18':
#             exit_program()
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()
