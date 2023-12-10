import random
import csv
import datetime

# List of sample first names and last names
first_names = ["John", "Jane", "Sam", "Sally", "Mike", "Emily", "James", "Jennifer", "Robert", "Linda", "Joseph", "Deanne", "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Helen", "Ivan", "Judy", "Kevin", "Laura", "Mark", "Nancy", "Oscar", "Paula", "Quentin", "Rachel", "Steve", "Tina", "Ulysses", "Victoria", "Walter", "Xena", "Yvonne", "Zach", "Aaron", "Beth", "Carl", "Dana", "Ethan", "Fiona", "Gary", "Hannah", "Ian", "Julia", "Kyle", "Lily"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Kemper", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards"]

# Function to generate a random email
def generate_email(first_name, last_name):
    domains = ["fakeschool.edu", "fakeschool1.edu", "fakeschool2.edu"]
    return f"{first_name.lower()}.{last_name.lower()}@{random.choice(domains)}"

# Function to generate a unique 10-digit student ID
def generate_student_id(existing_ids):
    while True:
        student_id = str(random.randint(1000000000, 9999999999))
        if student_id not in existing_ids:
            return student_id

# Function to generate a random date within the past 4 years
def generate_enrollment_date():
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=4*365)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

# Function to generate a date that is 4 years in the future from a given date
def generate_graduation_date(past_date):
    future_date = past_date + datetime.timedelta(days=4*365)
    return future_date



# Open the CSV file in write mode
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['student_id', 'first_name', 'last_name', 'email', 'enrollment_date', 'estimated_graduation_date'])
    # Generate and write 20 rows of fake data
    existing_ids = set()
    for _ in range(20):
        # Generate a random date within the past 4 years
        enrollment_date = generate_enrollment_date()

        # Generate a date that is 4 years in the future from the randomly chosen date
        estimated_graduation_date = generate_graduation_date(enrollment_date)
        
        student_id = generate_student_id(existing_ids)
        existing_ids.add(student_id)
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        email = generate_email(first_name, last_name)
        writer.writerow([student_id, first_name, last_name, email, enrollment_date, estimated_graduation_date])

