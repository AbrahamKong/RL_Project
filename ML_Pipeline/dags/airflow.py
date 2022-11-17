import logging
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.models import Variable
from ddpg import run

def rl_task():
    logging.info('Running RL Pipeline')
    run()
    logging.info('Done RL Pipeline')

default_args = {
    'owner': 'AllenWu',
    'start_date': datetime(2022, 11, 17),
    'schedule_interval': '@daily',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(dag_id='rl_pipeline', catchup=False, default_args=default_args) as dag:
    rl_task = PythonOperator(
        task_id='rl_task',
        python_callable=rl_task
    )
