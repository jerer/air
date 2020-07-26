import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator 


default_args = {
    'qq': '123',
    'start_date': datetime.datetime(2020, 7, 24),
    'kubernetes_labels': {'ll100': 'qqqqqqq'}
}

dag = DAG(
  'my_dag'
, schedule_interval = None
, default_args=default_args
)

op1 = BashOperator(task_id='dummy', bash_command='sleep 35', dag=dag,
   executor_config={
        "KubernetesExecutor": {"request_memory": "128Mi",
                               "limit_memory": "128Mi",}}

)
op2 = BashOperator(task_id='dummy100', bash_command='sleep 35', dag=dag,
executor_config={
        "KubernetesExecutor": {"request_memory": "128Mi",
                               "limit_memory": "128Mi",}}

)

# op1 >> op2
