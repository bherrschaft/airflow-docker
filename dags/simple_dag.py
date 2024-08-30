from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import shutil

# Define the function that will move the file
def move_file():
    source = '/usr/local/airflow/source_dir/text.txt'  # Path to the source file in the container
    destination = '/usr/local/airflow/dest_dir/text.txt'  # Path to the destination directory in the container
    shutil.move(source, destination)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 29),
    'retries': 1,
}

dag = DAG(
    'simple_dag',
    default_args=default_args,
    description='A simple DAG to move a file',
    schedule_interval='@daily',
)

start = DummyOperator(
    task_id='start',
    dag=dag,
)

# Create the PythonOperator that moves the file
move_file_task = PythonOperator(
    task_id='move_file',
    python_callable=move_file,
    dag=dag,
)

end = DummyOperator(
    task_id='end',
    dag=dag,
)

# Set the order of tasks
start >> move_file_task >> end
