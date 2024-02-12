
# Homework preparation
CREATE OR REPLACE EXTERNAL TABLE `direct-disk-412820.ny_taxi.green_taxi_2022`
OPTIONS(
  format = 'PARQUET',
  uris = ['gs://mage_data_engineering_zoomcamp/green_taxi_data_2022/green_tripdata_2022-*.parquet']
)

# Homework preparation

CREATE TABLE `direct-disk-412820.ny_taxi.green_taxi_2022_unpartitioned`
AS
SELECT *
FROM `direct-disk-412820.ny_taxi.green_taxi_2022`;


# Question 1
SELECT COUNT(*) AS record_count
FROM `direct-disk-412820.ny_taxi.green_taxi_2022_unpartitioned`;


# Question 2
-- Query for External Table
SELECT COUNT(DISTINCT PULocationID) AS distinct_PULocationIDs_external
FROM `direct-disk-412820.ny_taxi.green_taxi_2022`;

-- Query for Table
SELECT COUNT(DISTINCT PULocationID) AS distinct_PULocationIDs_table
FROM `direct-disk-412820.ny_taxi.green_taxi_2022_unpartitioned`;


# Question 3
SELECT COUNT(*)
FROM `direct-disk-412820.ny_taxi.green_taxi_2022_unpartitioned`
WHERE fare_amount = 0;


# Question 4
CREATE TABLE direct-disk-412820.ny_taxi.green_taxi_2022_partitioned_clustered
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID
OPTIONS(
    description = 'Partitioned and clustered table for 2022 Green Taxi data'
) AS
SELECT *
FROM direct-disk-412820.ny_taxi.green_taxi_2022;


# Question 5
-- Size of the non-partitioned table
SELECT
  table_id,
  ROUND(size_bytes / POW(2, 20), 2) AS size_mb
FROM
  `direct-disk-412820.ny_taxi.__TABLES__`
WHERE
  table_id = 'green_taxi_2022_unpartitioned';

-- Size of the partitioned table
SELECT
  table_id,
  ROUND(size_bytes / POW(2, 20), 2) AS size_mb
FROM
  `direct-disk-412820.ny_taxi.__TABLES__`
WHERE
  table_id = 'green_taxi_2022_partitioned_clustered';


# Question 8
SELECT count(*)
FROM `direct-disk-412820.ny_taxi.green_taxi_2022_partitioned_clustered`;
