from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from common.common_func import get_sftp ## /plugins 까지 하위 폴더로 잡게되면 에러 발생

with DAG(
    dag_id = "dags_python_import_func",
    schedule = "30 6 * * *",
    start_date = pendulum.datetime(2025, 4, 6, tz="Asia/Seoul"),
    catchup = False
) as dag:
    
    task_get_sftp = PythonOperator(
        task_id = 'task_get_sftp',
        python_callable = get_sftp
    )