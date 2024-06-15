INSTRUCTIONS
This Python application manages a job site, allowing users to create, update, and delete employers and jobs. Employers can create and manage job postings.

INSTALLATION
Clone the repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Ensure you have SQLite3 installed on your machine.
Usage
Run the cli.py file to start the CLI application.

Use the provided commands to interact with the application.
cli.py: Contains the main CLI interface for interacting with the application.
models/employer.py: Defines the Employer class for managing employers.
models/job.py: Defines the Job class for managing jobs.
helpers.py: Contains helper functions for the application.

COMMANDS
list_jobs: List all available jobs.
find_job_by_id: Find a job by its ID.
create_job: Create a new job.
update_job: Update an existing job.
delete_job: Delete a job.
list_jobs_by_employer: List all jobs by a specific employer.
list_employers: List all employers.
find_employer_by_id: Find an employer by their ID.
find_employer_by_name: Find an employer by their name.
create_employer: Create a new employer.
update_employer: Update an existing employer.
delete_employer: Delete an employer.
exit: Exit the program.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

