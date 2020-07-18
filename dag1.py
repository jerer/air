import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator


default_args = {
    'qq': '123',
    'start_date': datetime.datetime(2016, 1, 1),
}

dag = DAG('my_dag', default_args=default_args)
op = DummyOperator(task_id='dummy', dag=dag)
