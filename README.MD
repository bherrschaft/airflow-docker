# Airflow Docker Project

This project demonstrates the use of Apache Airflow within a Docker environment to automate a simple task: moving a text file from one directory to another. The setup is designed to be portable and easy to use across different systems. This guide will walk you through the steps to set up the environment and run the DAG.

## Prerequisites

Before you start, ensure you have the following installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- A Git client (e.g., [Git](https://git-scm.com/))

## Getting Started

### 1. Clone the Repository

First, clone the repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/airflow-docker-project.git
cd airflow-docker-project
```

### 2. Set Up the Directory Structure

Ensure the following directory structure exists within your project directory:

```plaintext
airflow-docker-project/
├── dags/
│   └── simple_dag.py
├── logs/
├── plugins/
├── source_dir/
│   └── text.txt  # This file will be moved by the DAG
├── dest_dir/
└── docker-compose.yml
```

### 3. Initialize the Airflow Environment

Run the following command to start the Airflow environment and initialize the database:

```bash
docker-compose up airflow-init
```

This command will:

- Initialize the Airflow database.
- Create a default user with the following credentials:
  - **Username:** airflow
  - **Password:** airflow

### 4. Start the Airflow Services

Once the initialization is complete, start the Airflow webserver and scheduler:

```bash
docker-compose up
```

This command will start the following services:

- **Postgres:** The database backend for Airflow.
- **Airflow Webserver:** The web interface to monitor and manage your DAGs.
- **Airflow Scheduler:** The service that schedules and triggers DAGs.

### 5. Access the Airflow Web UI

Once the services are up and running, you can access the Airflow web interface by navigating to:

```
http://localhost:8080
```

Log in with the default credentials:

- **Username:** airflow
- **Password:** airflow

### 6. Trigger the DAG

In the Airflow web interface, you should see a DAG named `simple_dag`. This DAG is scheduled to run daily and will move a file from the `source_dir` to the `dest_dir` within the Docker container.

To manually trigger the DAG:

1. Click on the toggle next to `simple_dag` to enable the DAG.
2. Click on the DAG name to view its details.
3. Click on the "Trigger DAG" button to manually start the process.

### 7. Verify the File Movement

After the DAG runs, you can verify that the `text.txt` file has been moved from the `source_dir` to the `dest_dir`. To do this:

1. Access the container's shell:
   ```bash
   docker exec -it airflow-docker_airflow-webserver_1 bash
   ```
2. Navigate to the destination directory:
   ```bash
   cd /usr/local/airflow/dest_dir
   ```
3. List the files:
   ```bash
   ls
   ```
   You should see the `text.txt` file in this directory.

### 8. Shutting Down

When you're done, you can stop all the services with:

```bash
docker-compose down
```

This command will stop and remove all the containers, but your data will persist in the volumes.

## Troubleshooting

- **File Not Found Error:** Ensure that the `text.txt` file exists in the `source_dir` before triggering the DAG.
- **DAG Not Showing Up:** If the DAG doesn't appear in the Airflow UI, check the logs to ensure that the DAG file is correctly placed in the `dags/` directory and that there are no syntax errors.

## Conclusion

This project provides a basic example of using Apache Airflow with Docker to automate file movements. You can expand on this by adding more complex workflows, integrating with different data sources, or scheduling more intricate tasks.

Feel free to modify the DAG, add more tasks, and explore the power of Apache Airflow!
