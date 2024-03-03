#!/bin/bash

set -e

# Check if two arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 [taxi_type] [year]"
    exit 1
fi

# Variables
TAXI_TYPE=$1
YEAR=$2
URL_PREFIX="https://github.com/DataTalksClub/nyc-tlc-data/releases/download"

# Loop over months
for MONTH in {1..12}; do
    FMONTH=$(printf "%02d" ${MONTH})  # Format month with leading zeros

    # Construct URL
    URL="${URL_PREFIX}/${TAXI_TYPE}/${TAXI_TYPE}_tripdata_${YEAR}-${FMONTH}.csv.gz"

    # Define local file path
    LOCAL_PREFIX="data/raw/${TAXI_TYPE}/${YEAR}/${FMONTH}"
    LOCAL_FILE="${TAXI_TYPE}_tripdata_${YEAR}_${FMONTH}.csv.gz"
    LOCAL_PATH="${LOCAL_PREFIX}/${LOCAL_FILE}"

    # Download data
    echo "Downloading ${URL} to ${LOCAL_PATH}"
    mkdir -p "${LOCAL_PREFIX}"  # Create local directory if it doesn't exist
    wget "${URL}" -O "${LOCAL_PATH}"
done
