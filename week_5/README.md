# Week 5

## ML Models Monitoring
ML models do degrade overtime, due to 
- Data Drift: In which new input data is no longer represented by the model's training dataset. Example: 3 new popular venues were opened in the last month, our Taxi duration model hasn't got samples of this new data in its training dataset

- Concept Drift: In which the concept changes, i.e: The relationship between inputs and outputs has changed (Not necessarily the data itself however).This drift as the name implies is due to "concepts" (i.e: hidden variables, underpinning hypotheses..etc) changing. Example: Taxi cars have been replaced by newer, faster, nimbler cars. Our model can no longer accurately predict trip durations


Monitoring ML models is mostly around monitoring four sectors:

- Service Health: General Software health check
- Model Performance: Depending on metrics for the problem
- Data Quality and integrity
- Data Drift & Concept Drift