from google.cloud import storage
import os

# Set the environment variable for service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/ndirangu749/direct-disk-412820-951f0087b486.json"


def upload_to_gcs(bucket_name, local_directory, destination_directory):
    """Uploads a directory of files to a GCS bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    # Iterate over files in the local directory
    for file_name in os.listdir(local_directory):
        if file_name.endswith('.parquet'):
            local_file_path = os.path.join(local_directory, file_name)
            blob = bucket.blob(os.path.join(destination_directory, file_name))
            blob.upload_from_filename(local_file_path, timeout=600)  # Set timeout
            print(f"Uploaded {local_file_path} to {destination_directory}/{file_name}")

# Usage
bucket_name = 'mage_data_engineering_zoomcamp'
local_directory = '/home/ndirangu749/ZOOMCAMP/Data_Engineering_Zoomcamp_2024/module_4_analytics_engineering/data'
destination_directory = 'fhv_ny_taxi_2019'

upload_to_gcs(bucket_name, local_directory, destination_directory)
