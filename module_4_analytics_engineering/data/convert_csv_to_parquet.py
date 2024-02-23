import pandas as pd

data_types = {
    'dispatching_base_num': 'object',
    'PUlocationID': 'float64',
    'DOlocationID': 'float64',
    'SR_Flag': 'float64',
    'Affiliated_base_number': 'object',
}
date_cols = ['pickup_datetime', 'dropOff_datetime']

def convert_to_parquet(year, service):
    for i in range(1, 13):
        month = f'{i:02}'  # Format month as two digits with leading zero
        csv_file_name = f"{service}_tripdata_{year}-{month}.csv.gz"
        parquet_file_name = f"{service}_tripdata_{year}-{month}.parquet"

        # Read CSV file directly from the local directory
        df = pd.read_csv(csv_file_name, compression='gzip', dtype=data_types, parse_dates=date_cols)

        # Convert DataFrame to Parquet format
        df.to_parquet(parquet_file_name, engine='pyarrow')

        print(f"Converted {csv_file_name} to {parquet_file_name}")

# usage:
convert_to_parquet(2019, 'fhv')