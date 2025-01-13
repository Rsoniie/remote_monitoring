
from faker import Faker
import json
import random
from datetime import datetime



def generate_random_user():
    fake = Faker()
    random_name = fake.name()
    random_email = fake.email()

    user_data = {
        "username": random_name,
        "email": random_email,
        "health_data": [],
        "created_at": datetime.utcnow()
    }
    return user_data


def genrate_random_health_data():
    heart_rate = random.randint(60, 100) 
    blood_pressure = f"{random.randint(90, 140)}/{random.randint(60, 90)}"
    sleep_duration = round(random.uniform(4, 10), 1) 
    oxygen_level = random.randint(90, 100)  
    stress_level = random.randint(1, 10) 
    skin_temp = round(random.uniform(95.0, 99.5), 1)

    health_data = {
        "heart_rate": heart_rate,
        "blood_pressure": blood_pressure,
        "sleep_duration": sleep_duration,
        "oxygen_level": oxygen_level,
        "stress_level": stress_level,
        "skin_temp": skin_temp
    }

    return health_data
