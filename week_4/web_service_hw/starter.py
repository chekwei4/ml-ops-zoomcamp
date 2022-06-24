import sys

import pickle
import pandas as pd
import statistics
import pyarrow

with open('model.bin', 'rb') as f_in:
    dv, lr = pickle.load(f_in)

categorical = ['PUlocationID', 'DOlocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.dropOff_datetime - df.pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df

def get_prediction():
    input_year = str(sys.argv[1])
    input_month = str(sys.argv[2])
    
    df = read_data(f'https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_{input_year}-{input_month}.parquet')

    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = lr.predict(X_val)
    print(f"mean prediction for {input_year}.{input_month} : {statistics.mean(y_pred)}")
    # return df, y_pred

def prepare_dataframe():
    df, y_pred = get_prediction()

    year = "2021"
    month = "02"

    df['ride_id'] = f'{year}/{month}_' + df.index.astype('str')
    df["y_pred"] = y_pred
    df_result = df[["ride_id", "y_pred"]]
    df_result.to_parquet(
            "df_parquet",
            engine='pyarrow',
            compression=None,
            index=False
            )

# prepare_dataframe()

get_prediction()
