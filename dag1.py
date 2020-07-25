import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator 


default_args = {
    'qq': '123',
    'start_date': datetime.datetime(2020, 7, 24),
    'schedule_interval': None
}

dag = DAG('my_dag', default_args=default_args)
op1 = BashOperator(task_id='dummy', bash_command='sleep 10', dag=dag)
op2 = BashOperator(task_id='dummy100', bash_command='sleep 10', dag=dag)

op1 >> op2
