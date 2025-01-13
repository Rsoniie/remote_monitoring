
from faker import Faker
import json

def generate_random_user():
    fake = Faker()
    random_name = fake.name()
    random_email = fake.email()

    user_data = {
        "username": random_name,
        "email": random_email
    }

    # Convert to JSON format and return
    # return json.dumps(user_data, indent=4)
    return user_data
