# ML Ops Zoomcamp

## Week 1 - Intro
[Notes](https://github.com/chekwei4/ml-ops-zoomcamp/tree/main/week_1)
- What is MLOps
- MLOps maturity model
- Running example: NY Taxi trips dataset
- Why do we need MLOps
- Course overview


## Week 2 - Experiment Tracking
[Notes](https://github.com/chekwei4/ml-ops-zoomcamp/tree/main/week_2)
- Experiment tracking intro
- Getting started with MLflow
- Experiment tracking with MLflow
  - Run hyperparameter tuning using Hyperopt, and then logging all the run results in MLflow
- Saving and loading models with MLflow
- Promoting best model to Model registry
    - Filter out some of the best performing models on validation sets, run them through test set, thereby promoting the best model to model registry

## Week 3 - Orchestration and ML Pipelines
[Notes](https://github.com/chekwei4/ml-ops-zoomcamp/tree/main/week_3)
- Workflow orchestration
- Prefect 2.0
    - Concept of task and flow
    - Work-queues and agents
    - Previewing work-queues and view scheduled runs
    - IntervalSchedule vs CronSchedule
- Created a mini project that downloaded, ingested, trained and validated on datasets automatically based on a scheduled interval time period. 


## Week 4 - Deploying Models with Flask and Docker
- Creating a new virtual environment
- Create a script for prediction
- Put script into Flask app
- Dockerize the app


credits: DataTalksCub

author: chekwei