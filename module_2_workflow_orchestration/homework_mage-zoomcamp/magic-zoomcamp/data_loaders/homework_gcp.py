from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
import pyarrow.parquet as pq

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

@data_loader
def load_from_google_cloud_storage(*args, **kwargs):
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    bucket_name = 'mage_data_engineering_zoomcamp'  # Replace with your bucket name
    table_name = "nyc_taxi_data"  # Replace with your table name
    object_key = f"{table_name}/"  # Adjust as needed

    gcs = GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile))
    dataset = pq.ParquetDataset(
        f"gs://{bucket_name}/{object_key}", filesystem=gcs.filesystem
    )
    table = dataset.read()
    return table.to_pandas()
