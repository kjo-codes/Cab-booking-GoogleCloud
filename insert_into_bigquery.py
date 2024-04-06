from google.cloud import bigquery

# Initialize BigQuery client
client = bigquery.Client()

# Define the dataset and table for cab bookings
bookings_dataset_id = 'cab-booking-system-419219.B11'
bookings_table_id = 'cab-booking-system-419219.B11.tb_11'

# Define the dataset and table for available cabs
cabs_dataset_id = 'cab-booking-system-419219.C11'
cabs_table_id = 'cab-booking-system-419219.C11.tc_11'

def insert_booking(pickup, destination):
    # Insert booking data into BigQuery
    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("pickup", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("destination", "STRING", mode="REQUIRED"),
        ],
        write_disposition='WRITE_APPEND'
    )

    rows_to_insert = [
        {"pickup": pickup, "destination": destination}
    ]

    client.insert_rows_json(bookings_table_id, rows_to_insert, job_config=job_config)

def insert_cab(driver_name, current_location):
    # Insert cab data into BigQuery
    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("driver_name", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("current_location", "STRING", mode="REQUIRED"),
        ],
        write_disposition='WRITE_APPEND'
    )

    rows_to_insert = [
        {"driver_name": driver_name, "current_location": current_location}
    ]

    client.insert_rows_json(cabs_table_id, rows_to_insert, job_config=job_config)

# Example usage
insert_booking("123 Main St", "456 Elm St")
insert_cab("John Doe", "789 Oak St")
