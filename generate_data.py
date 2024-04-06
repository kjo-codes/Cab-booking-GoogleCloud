from faker import Faker
import csv

fake = Faker()

# Generate sample bookings data
def generate_bookings_data(num_records):
    bookings = []
    for _ in range(num_records):
        booking = {
            'booking_id': fake.random_int(min=1000, max=9999),
            'user_id': fake.random_int(min=1, max=100),
            'cab_id': fake.random_int(min=1, max=50),
            'pickup_location': fake.street_address(),
            'destination': fake.street_address(),
            'booking_time': fake.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%d %H:%M:%S')
        }
        bookings.append(booking)
    return bookings

# Generate sample cabs data
def generate_cabs_data(num_records):
    cabs = []
    for cab_id in range(1, num_records + 1):
        cab = {
            'cab_id': cab_id,
            'driver_name': fake.name(),
            'current_location': fake.street_address()
        }
        cabs.append(cab)
    return cabs

# Write data to CSV files
def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for record in data:
            writer.writerow(record)

# Generate bookings data and write to CSV file
bookings_data = generate_bookings_data(100)  # Adjust the number of records as needed
write_to_csv(bookings_data, 'bookings.csv')

# Generate cabs data and write to CSV file
cabs_data = generate_cabs_data(50)  # Adjust the number of records as needed
write_to_csv(cabs_data, 'cabs.csv')

print("Sample data generation completed successfully.")
