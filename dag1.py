import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator 


default_args = {
    'qq': '123',
    'start_date': datetime.datetime(2020, 88888888, 24),
}

dag = DAG('my_dag', default_args=default_args)
op = BashOperator(task_id='dummy', bash_command='echo 1', dag=dag)
