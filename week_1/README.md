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
