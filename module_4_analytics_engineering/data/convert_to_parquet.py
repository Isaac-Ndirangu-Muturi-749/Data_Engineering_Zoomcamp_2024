import pandas as pd

def convert_to_parquet(year, service):
    for i in range(1, 13):
        month = f'{i:02}'  # Format month as two digits with leading zero
        csv_file_name = f"{service}_tripdata_{year}-{month}.csv.gz"
        parquet_file_name = f"{service}_tripdata_{year}-{month}.parquet"

        # Read CSV file directly from the local directory
        df = pd.read_csv(csv_file_name, compression='gzip')

        # Convert DataFrame to Parquet format
        df.to_parquet(parquet_file_name, engine='pyarrow')

        print(f"Converted {csv_file_name} to {parquet_file_name}")

# Example usage:
convert_to_parquet(2019, 'fhv')
