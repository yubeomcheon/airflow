from airflow import DAG
import pendulum
import datetime
from airflow.operators.email import EmailOperator

with DAG(
    dag_id = "dags_email_operator",
    schedule = "0 8 1 * *",
    start_date = pendulum.datetime(2025, 4, 6, tz="Asia/Seoul"),
    catchup = False
) as dag:
    send_email_task = EmailOperator(
        task_id = 'send_email_task',
        to = 'bum8242@naver.com',
        subject = 'airflow 성공'
        html_content= 'Airflow 작업 완료'
    )