from azure.ai.ml.entities import Environment
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient.from_config(credential=DefaultAzureCredential())

my_env = Environment(
    name="training-env",
    description="Environment for training model",
    conda_file="train-conda.yaml",  # or whatever your YAML file is called
    image="mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu20.04:latest"
)

ml_client.environments.create_or_update(my_env)
