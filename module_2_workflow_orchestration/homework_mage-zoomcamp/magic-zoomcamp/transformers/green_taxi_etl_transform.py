if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform_data(data, *args, **kwargs):
    # Remove rows where passenger count is equal to 0 or trip distance is equal to 0
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to date
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # Rename columns from Camel Case to Snake Case
    data.rename(columns={
        'VendorID': 'vendor_id',
        'RatecodeID': 'ratecode_id',
        'PULocationID': 'pu_location_id',
        'DOLocationID': 'do_location_id',
    }, inplace=True)

    return data

@test
def test_output(output, *args) -> None:
    # Add assertions
    # Assertion: vendor_id is one of the columns
    assert 'vendor_id' in output.columns, 'vendor_id column not found in the dataset'
    assert (output['passenger_count'] > 0).all(), 'Invalid passenger_count values'
    assert (output['trip_distance'] > 0).all(), 'Invalid trip_distance values'
