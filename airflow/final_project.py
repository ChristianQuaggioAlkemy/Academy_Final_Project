from datetime import timedelta
import os

from airflow import DAG 
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import datetime
from airflow.utils.dates import timedelta



with DAG(
    dag_id='dbt_final_project',
    start_date=datetime(2022, 8, 1),
    description='An Airflow DAG to execute dbt commands for our final project',
    schedule_interval=timedelta(days=1)
) as dag:

    dbt_test = BashOperator (
        task_id='test',
        bash_command='cd /app/dbt/final_project && dbt test'
    )
    
    dwh_earthquake_data = BashOperator (
        task_id='dwh_earthquake_data',
        bash_command='cd /app/dbt/final_project && dbt run --select dwh_earthquake_data.sql'
    )    

    dwh_countries_info = BashOperator (
        task_id='dwh_countries_info',
        bash_command='cd /app/dbt/final_project && dbt run --select dwh_countries_info.sql'
    ) 

    dwh_index_stock_data = BashOperator (
        task_id='dwh_index_stock_data',
        bash_command='cd /app/dbt/final_project && dbt run --select dwh_index_stock_data.sql'
    ) 
    
    index_variation = BashOperator (
        task_id='index_variation',
        bash_command='cd /app/dbt/final_project && dbt run --select index_variation.sql'
    )
    
    earthquake_index_join = BashOperator (
        task_id='earthquake_index_join',
        bash_command='cd /app/dbt/final_project && dbt run --select earthquake_index_join.sql'
    )
    
    earthquake_countries_join = BashOperator (
        task_id='earthquake_countries_join',
        bash_command='cd /app/dbt/final_project && dbt run --select earthquake_countries_join.sql'
    )
    
    earthquake_data_dummies = BashOperator (
        task_id='earthquake_data_dummies',
        bash_command='cd /app/dbt/final_project && dbt run --select earthquake_data_dummies.sql'
    )
    
    earthquake_data_perception = BashOperator (
        task_id='earthquake_data_perception',
        bash_command='cd /app/dbt/final_project && dbt run --select earthquake_data_perception.sql'
    )
    
    dwh_earthquake_data << dbt_test
    dwh_countries_info << dbt_test
    dwh_index_stock_data << dbt_test
    index_variation << dwh_index_stock_data
    earthquake_data_dummies << dwh_earthquake_data
    earthquake_data_perception << dwh_earthquake_data
    earthquake_countries_join << dwh_countries_info
    earthquake_countries_join << earthquake_data_perception
    earthquake_index_join << earthquake_data_dummies
    earthquake_index_join << index_variation
