# Week 2

## Experiment Tracking
Proces of keeping tracking of all the relevant info from an ML experiment, includes:
- source code
- environment
- data
- model
- hyperparams
- metrics

### Why experiment tracking is important?
- reproducibility
- organisation
  - collaborating with different people in the team
- optimization

## Using MLflow
- An open source platform for the ML lifecycle.
- An ML experiment is the process of building an ML model
  - One experiment is basically a bunch of ML runs associated
- Experiment run: Each trial in an ML experiment
- Just a python package that can be installed with pip and contains four main modules:
  1. tracking
    - Allow u to organise your experiments into runs
    - Able to keep track params, metrics, metadata, artifacts, models
      - Metrics like accuracy, F1 score
      - Metadata includes any info related to the info. Let us search and filter the experiments easily
      - Artifacts like any visualisation files that can be logged
      - Models can be logged too
  2. models
  3. model registry
    - useful for model tracking 
  4. projects
- MLflow will auto log extra info:
  - source code
  - git commit (version of the code)
  - start, end time
  - author

## Run MLflow

```
pip install mlflow

mlflow --version
```
`mlflow, version 1.26.1`

To launch MLflow, remember to initiate with a backend DB.

```
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Within the python code, we need to import MLflow, just like any other packages. 

```python
import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("my-brand-new-experiment")
```
The backend DB which we initiated was `sqlite:///mlflow.db`, so we will use that as our `tracking_uri`.

Below is a sample way to log metrics, create tags, and alpha value for a linear regression experiment run. 

```python
with mlflow.start_run():

    mlflow.set_tag("developer", "cristian")

    mlflow.log_param("train-data-path", "./data/green_tripdata_2021-01.csv")
    mlflow.log_param("valid-data-path", "./data/green_tripdata_2021-02.csv")

    alpha = 0.1
    mlflow.log_param("alpha", alpha)
    lr = Lasso(alpha)
    lr.fit(X_train, y_train)

    y_pred = lr.predict(X_val)
    rmse = mean_squared_error(y_val, y_pred, squared=False)
    mlflow.log_metric("rmse", rmse)
```