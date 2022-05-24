# Week 1 Homework
The goal of this homework is to train a simple model for predicting the duration of a ride.

## Question 1
- Download For-Hire Vehicle Trip Records
- January 2021 and February 2021
- Number of records on Jan 2021 FHV data:
- 1154112 entries
```python
df = pd.read_parquet("fhv_tripdata_2021-01.parquet")

df.info()
```

## Question 2
- Average duration in Jan 2021 FHV
- Create a new feature called `travel_duration` that finds the difference between `dropOff_datetime` and `pickup_datetime`
```python
df["travel_duration"] = df["dropOff_datetime"] - df["pickup_datetime"]
```
- Next, we need to convert the values in `travel_duration` to minutes

```python
df["travel_duration"] = df["travel_duration"].apply(lambda td: td.total_seconds()/60)

df["travel_duration"].mean()
```
- 19.17

## Question 3
- We only want to keep data where `travel_duration` is between 1 - 60 minutes (inclusive) 
``` python
df.drop(df[df.travel_duration > 60].index, inplace=True)
df.drop(df[df.travel_duration < 1].index, inplace=True)v
```
- Fraction of missing values for `PUlocationID`
- 83.527328

## Question 4
- Dimensionality after OHE
- Apply OHE to the pickup and dropoff location IDs
- We'll use only these two features for our model
- Total number of columns (features) after applying one-hot encoding: 525 columns
- After dict vectorizer, we have 525 columns

Snippets of code below:

```python
from sklearn.feature_extraction import DictVectorizer
categorical = ['PUlocationID', 'DOlocationID']
numerical = ['travel_duration']

train_dicts = df_fill_na[categorical].to_dict('records')
dict_vect = DictVectorizer()
X_train = dict_vect.fit_transform(train_dicts)

X_train.shape 
```
- (1109826, 525)

## Question 5
- Evaluate on train data
- RMSE: 10.53

## Question 6 
- Evaluate on unseen test data
- RMSE: 12.85