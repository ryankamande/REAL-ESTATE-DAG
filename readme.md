# Real Estate DAG

A workflow automation project utilizing Directed Acyclic Graphs (DAGs) for efficient real estate data processing.

## Features

- Automated data ingestion and transformation
- Task orchestration with DAG-based workflows
- Modular, extensible architecture for easy customization

## PostgreSQL Configuration

1. **Install PostgreSQL**  
    Download and install PostgreSQL from [https://www.postgresql.org/download/](https://www.postgresql.org/download/).

2. **Create a Database and User**
     ```sql
     CREATE DATABASE real_estate_db;
     CREATE USER real_estate_user WITH PASSWORD 'yourpassword';
     GRANT ALL PRIVILEGES ON DATABASE real_estate_db TO real_estate_user;
     ```

3. **Update Configuration**  
    Set your PostgreSQL connection details in `config.yaml` or as environment variables:
     ```yaml
     postgres:
        host: localhost
        port: 5432
        database: real_estate_db
        user: real_estate_user
        password: yourpassword
     ```

## Apache Airflow Configuration

1. **Install Apache Airflow**
     ```bash
     pip install apache-airflow
     ```

2. **Initialize Airflow Database**
     ```bash
     airflow db init
     ```

3. **Configure Airflow Connections**
     - Set up a PostgreSQL connection in Airflow:
        ```bash
        airflow connections add 'real_estate_postgres' \
          --conn-type 'postgres' \
          --conn-host 'localhost' \
          --conn-login 'real_estate_user' \
          --conn-password 'yourpassword' \
          --conn-schema 'real_estate_db' \
          --conn-port 5432
        ```

4. **Start Airflow Webserver and Scheduler**
     ```bash
     airflow webserver --port 8080
     airflow scheduler
     ```

## Getting Started

1. **Clone the repository**
     ```bash
     git clone https://github.com/ryankamande/real-estate-dag.git
     cd real-estate-dag
     ```

2. **Install dependencies**
     ```bash
     pip install -r requirements.txt
     ```

3. **Configure settings**
     - Update `config.yaml` or set environment variables as needed.

4. **Run the workflow**
     ```bash
     python main.py
     ```

## Project Structure

```
real-estate-dag/
├── dags/
├── data/
├── scripts/
├── requirements.txt
└── README.md
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

Licensed under the MIT License.