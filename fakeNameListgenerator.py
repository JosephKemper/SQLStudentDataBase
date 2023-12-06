import random
import csv

# List of sample first names and last names
first_names = ["John", "Jane", "Sam", "Sally", "Mike", "Emily", "James", "Jennifer", "Robert", "Linda"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

# Function to generate a random email
def generate_email(first_name, last_name):
    domains = ["fakeschool.edu", "fakeschool1.edu", "fakeschool2.edu"]
    return f"{first_name.lower()}.{last_name.lower()}@{random.choice(domains)}"

# Open the CSV file in write mode
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['first_name', 'last_name', 'email'])
    # Generate and write 20 rows of fake data
    for _ in range(20):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        email = generate_email(first_name, last_name)
        writer.writerow([first_name, last_name, email])