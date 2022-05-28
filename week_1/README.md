# Week 1 

## Putting Machine Learning to Production
What ML Ops is actually? 
- A set of best practices for putting Machine Learning in production.

## Stages of an ML project
1. Design
We see if machine learning is the right tool for solving the problem.
Do we really need ML here? 
If yes, we go to the next step.

2. Train
Train the model. Find the best possible model, do a lot of different experiment. End of the stage, we expect a model that we can use and apply all the new data we have in the next stage.

3. Operate
We can choose to deploy the model to some sort of a web service through an API, and then the customers from the phone can communicate with the API and tell the application where they want to go (drop-off location). Then our API will tell the customer that the trip will approximately take ~10 mins. This process is called deployment, and this is done as part of the operate stage.

How do we make sure that the model is performing well? 
- It does not degrade, it does not perform worse.

All the steps like experimenting with different models, reproducing the results, retraining the model easily with one click, easily deploy the model, and we can monitor the quality of this model are part of the best practices of MLOps.

## Experiment Tracking and Model Management
- Instead of relying on spreadsheets, or manual notes on jupyter notebooks, we can use tools to help us track/log our experiments (Eg. Lasso, Ridge, Linear Regression performances)

- Saving models in model registry, where model registry will keep all the trained models together with the experiment metrics

- Both experiment tracker and model registry can be used together and work hand in hand.

## Machine Learning Pipeline
One of the example workflows:
- Load and Prepare data -> Vectorize -> Train

Idea of parameterize the workflows:
Sample command to run the pipeline can be:
- `python pipeline.py --train_data <...> --val_data <...>`


Sample tools
- Prefect, Kubeflow Pipelines etc.

## Deploying the Model
- Serve the model to our users through a web service

## Monitoring the Model
- Auto retrain and redeploy the ML model without human interventions

## MLOps Maturity Model
- Different level of maturity 
    - Level 0: no MLOps automation at all. Eg. Pure jupyter notebook. Mainly for POC.
    - Level 1: DevOps, but no MLOps. Releases (deployment of models) are automated, there's CI/CD. Presence of unit testings and integration testings to make sure that the model doesn't break anything in deployment. Generally not ML aware. No experiment tracking, no model reproducibility. 
    - Level 2: Automated Training. There's training pipeline, experiment tracking, model registry. Low friction deployment.
    - Level 3: Automated Deployment. No need human to deploy the models. Call an API to deploy a model on model platform. Presence of monitoring too.
      - Data Prep -> Train Model -> Deploy Model
      - Ability to run A/B test to see which model (A or B) works better
    - Level 4: Full MLOps automation. Auto training, retraining, deployment. 