import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(*args, **kwargs):
    base_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green'
    taxi_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RatecodeID': pd.Int64Dtype(),
        'store_and_fwd_flag': str,
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'payment_type': pd.Int64Dtype(),
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'congestion_surcharge': float
    }
    # native date parsing 
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    dfs = []  # List to store DataFrames for each month

    # Load data for the final three months (10, 11, 12) using a for loop
    for month in range(10, 13):
        url = f'{base_url}/green_tripdata_2020-{month}.csv.gz'
        df = pd.read_csv(url, sep=',', compression='gzip', dtype=taxi_dtypes, parse_dates=parse_dates)
        dfs.append(df)

    # Concatenate DataFrames for the final quarter
    final_quarter_data = pd.concat(dfs, ignore_index=True)
    data = final_quarter_data
    return data

@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
