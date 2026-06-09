from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "lucas",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}


with DAG(
    dag_id="api_data_ingestion_pipeline",
    description="Pipeline API -> Bronze -> Silver -> Gold",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["data-engineering", "api", "medallion"],
) as dag:

    extract = BashOperator(
        task_id="extract_api_data",
        bash_command="cd /mnt/c/Users/Usuário/Documents/projetos-engenharia-de-dados/api-data-ingestion-pipeline && python3 src/extract.py",
    )

    bronze = BashOperator(
        task_id="bronze_layer",
        bash_command="cd /mnt/c/Users/Usuário/Documents/projetos-engenharia-de-dados/api-data-ingestion-pipeline && python3 src/bronze.py",
    )

    silver = BashOperator(
        task_id="silver_layer",
        bash_command="cd /mnt/c/Users/Usuário/Documents/projetos-engenharia-de-dados/api-data-ingestion-pipeline && python3 src/silver.py",
    )

    gold = BashOperator(
        task_id="gold_layer",
        bash_command="cd /mnt/c/Users/Usuário/Documents/projetos-engenharia-de-dados/api-data-ingestion-pipeline && python3 src/gold.py",
    )

    extract >> bronze >> silver >> gold