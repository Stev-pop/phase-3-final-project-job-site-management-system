from models.employee import Employee
from models.job import Job
from lib.models.employer import Employee_Job

from helpers import (
    exit_program,
    list_jobs,
    find_job_by_id,
    create_job,
    update_job,
    delete_job,
    list_jobs_by_employer,
    list_employees_for_job,
    list_jobs_for_employee,
    assign_employee_to_job,
    unassign_employee_from_job
)

def main():
    Employee.create_table()
    Job.create_table()
    Employee_Job.create_table()

    while True:
        print("\nJob Site Management System")
        print("1. Create Job")
        print("2. List Jobs")
        print("3. Find Job by ID")
        print("4. Update Job Post")
        print("5. Delete Job")
        print("6. List Jobs by Employer")
        print("7. List Employees for Job")
        print("8. List Jobs for Employee")
        print("9. Assign Employee to Job")
        print("10. Unassign Employee from Job")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_job()
        elif choice == '2':
            list_jobs()
        elif choice == '3':
            find_job_by_id()
        elif choice == '4':
            update_job()
        elif choice == '5':
            delete_job()
        elif choice == '6':
            list_jobs_by_employer()
        elif choice == '7':
            list_employees_for_job()
        elif choice == '8':
            list_jobs_for_employee()
        elif choice == '9':
            assign_employee_to_job()
        elif choice == '10':
            unassign_employee_from_job()
        elif choice == '0':
            exit_program()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
