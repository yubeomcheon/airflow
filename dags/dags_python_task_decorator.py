from airflow import DAG
import pendulum
from airflow.decorators import task



with DAG(
    dag_id = "dags_python_task_decorator",
    schedule = pendulum.datetime(2025, 4, 5, tz = "Asia/Seoul"),
    catchup = False,
) as dag:
    
    @task(task_id = "python_task_1")
    def print_context(some_input):
        print(some_input)
    
    python_task_1 = print_context("task_decorator 실행")