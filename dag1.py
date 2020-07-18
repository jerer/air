from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator


default_args = {
    'qq': '123',
}

dag = DAG('my_dag', default_args=default_args)
op = DummyOperator(task_id='dummy', dag=dag)
