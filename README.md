# end-to-end-mlflow


https://dagshub.com/rakeshmr09/end-to-end-mlflow.mlflow

import dagshub
dagshub.init(repo_owner='rakeshmr09', repo_name='end-to-end-mlflow', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)