{{ config(materialized='table') }}

-- Common Table Expressions (CTEs) to prepare the data
with fhv as (
    -- Select all columns from the staging FHV table
    select * 
    from {{ ref('stg_fhv_tripdata') }}
), 
dim_zones as (
    -- Select all columns from the zones dimension table
    select * 
    from {{ ref('dim_zones') }}
    -- Filter out rows where the borough is 'Unknown'
    where borough != 'Unknown'
)

-- Main query to select and transform data
select 
    -- Selecting trip-related information
    fhv.tripid,
    fhv.pickup_locationid,
    fhv.dropoff_locationid,
    fhv.pickup_datetime,
    fhv.dropoff_datetime,
    fhv.dispatching_base_num,
    fhv.sr_flag,
    fhv.affiliated_base_number,
    -- Selecting additional information from pickup and dropoff zones
    pickup_zone.borough as pickup_borough, 
    pickup_zone.zone as pickup_zone, 
    dropoff_zone.borough as dropoff_borough, 
    dropoff_zone.zone as dropoff_zone
-- Joining with the dim_zones table to get borough and zone information
from fhv
inner join dim_zones as pickup_zone
    on fhv.pickup_locationid = pickup_zone.locationid
inner join dim_zones as dropoff_zone
    on fhv.dropoff_locationid = dropoff_zone.locationid
