from models.employer import Employer
from models.job import Job
from models.employee import Employee

from helpers import (
    exit_program,
    list_jobs,
    find_job_by_id,
    create_job,
    update_job,
    delete_job,
    list_jobs_by_employer,
    list_employers,
    find_employer_by_id,
    create_employer,
    update_employer,
    delete_employer,
    find_jobs_with_employer_names_input,
    list_employees,
    find_employee_by_id,
    create_employee,
    update_employee,
    delete_employee
)

def main():
    Employer.create_table()
    Job.create_table()
    Employee.create_table()

    while True:
        print("\nJob Site Management System")
        print("1. Create Job")
        print("2. List Jobs")
        print("3. Find Job by ID")
        print("4. Update Job Post")
        print("5. Delete Job")
        print("6. List Jobs by Employer")
        print("7. List Employers")
        print("8. Find Employer by ID")
        print("9. Create Employer")
        print("10. Update Employer")
        print("11. Delete Employer")
        print("12. Find Jobs with Employer Names")
        print("13. List Employees")
        print("14. Find Employee by ID")
        print("15. Create Employee")
        print("16. Update Employee")
        print("17. Delete Employee")
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
            list_employers()
        elif choice == '8':
            find_employer_by_id()
        elif choice == '9':
            create_employer()
        elif choice == '10':
            update_employer()
        elif choice == '11':
            delete_employer()
        elif choice == '12':
            find_jobs_with_employer_names_input()
        elif choice == '13':
            list_employees()
        elif choice == '14':
            find_employee_by_id()
        elif choice == '15':
            create_employee()
        elif choice == '16':
            update_employee()
        elif choice == '17':
            delete_employee()
        elif choice == '0':
            exit_program()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
