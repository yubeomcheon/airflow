from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from commmon.common_fun import regist

with DAG(
    dag_is = "dags_python_with_op_args",
    schedule = "30 6 * * *",
    start_date = pendulum.datetime(2025, 4, 5, tv = "Asia/Seoul"),
    catchup = False
) as dag:
    regist_t1 = PythonOperator(
        task_id = 'regist_t1',
        python_callable = regist,
        op_args = ['hjjim', 'man', 'kr', 'seoul']
    )
    
    regist_t1