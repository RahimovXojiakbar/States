import os
import random
import django
from random import choice



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from faker import Faker
from main import models


# models.State.objects.all().delete()
models.Region.objects.all().delete()
models.District.objects.all().delete()
models.MFY.objects.all().delete()
models.Neighborhood.objects.all().delete()
models.House.objects.all().delete()
models.Human.objects.all().delete()






fake = Faker()


flag_images = [
    'flags/istockphoto-1417699870-1024x1024.jpg',
    'flags/istockphoto-1132287964-1024x1024.jpg',
    'flags/istockphoto-1417699847-1024x1024.jpg',
    'flags/istockphoto-1414559861-1024x1024.jpg',
    'flags/istockphoto-1282495978-1024x1024.jpg'
]

emblem_images = [
    'emblems/istockphoto-2170922539-1024x1024.jpg' 
    'emblems/istockphoto-1126122253-1024x1024.jpg' 
    'emblems/istockphoto-1315926501-1024x1024.jpg' 
    'emblems/istockphoto-960107412-1024x1024.jpg'
]


# =======================================================================================================

# for _ in range(15):

#     states = models.State.objects.create(
#         continent = fake.random_element(['Afrika', 'Amerika', 'Asia', 'Europa', 'Oceania']),
#         title = fake.word().capitalize(),
#         president = fake.name_male(),
#         about = fake.text(max_nb_chars=60),
#         flag = random.choice(flag_images),
#         anthem = fake.text(max_nb_chars=200),
#         emblem = random.choice(emblem_images),
#         language = fake.word().capitalize(),
#         area_km_kv = round(random.uniform(100, 900), 2),
#         people = round(random.uniform(1000000, 100000000)),
#         capital = fake.word().capitalize(),
#         gdp = round(random.uniform(50, 500), 2),
#         unemployment_rate = fake.random_int(min=5, max=20),
#         inflation_rate = fake.random_int(min=3, max=15),
#         poverty_rate = fake.random_int(min=5, max=30),
#         literacy_rate = fake.random_int(min=85, max=100),
#         life_expectancy = fake.random_int(min=60, max=85),
#         population_growth_rate = fake.random_int(min=1, max=10),
#         urban_population_percentage = fake.random_int(min=40, max=90),
#         birth_rate = fake.random_int(min=10, max=40),
#         death_rate = fake.random_int(min=5, max=15)

#     )
#     states.save()
models.State.objects.all()
print('Add States')


# =======================================================================================================

for _ in range(50):
    regions = models.Region.objects.create(
        title = fake.word().capitalize(),
        state = choice(models.State.objects.all()),
        governor = fake.name_male(),
        about = fake.text(max_nb_chars=200),
        people = round(random.uniform(100000, 10000000)),
        total_area_km2=round(random.uniform(1000, 50000), 2),
        population_density=round(random.uniform(50, 1000)),
        gdp=round(random.uniform(19, 112), 2),
        unemployment_rate=round(random.uniform(0, 20), 2),
        literacy_rate=round(random.uniform(80, 100), 2),
        median_income=round(random.uniform(50, 1500), 2)
    )
    regions.save()
models.Region.objects.all()
print('Add Regions')


# =======================================================================================================

for _ in range(150):
    districts = models.District.objects.create(
        title = fake.word().capitalize(),
        region = choice(models.Region.objects.all()),
        governor = fake.name_male(),
        about = fake.text(max_nb_chars=200),
        area_km_kv = round(random.uniform(100, 5000), 2),
        people = round(random.uniform(100000, 10000000)),
        total_budget=round(random.uniform(18, 510), 2),
        poverty_rate=round(random.uniform(5, 50), 2),
        literacy_rate=round(random.uniform(75, 100), 2),
        unemployment_rate=round(random.uniform(2, 25), 2),
        healthcare_facilities=random.randint(5, 50),
        educational_institutions=random.randint(10, 200),
        industrial_units=random.randint(5, 100),
        average_income_per_person=round(random.uniform(200, 2000), 2),
        birth_rate=round(random.uniform(10, 40), 2),
        death_rate=round(random.uniform(5, 20), 2),
    )
    districts.save()
models.District.objects.all()
print('Add Districts')



# =======================================================================================================

for _ in range(500):
    mfy = models.MFY.objects.create(
        title=fake.word().capitalize(),
        district=choice(models.District.objects.all()),
        chairman=fake.name_male(),
        area_km_kv=round(random.uniform(10, 100), 2),
        people=random.randint(5000, 30000),
        total_budget=round(random.uniform(18, 510), 2),
        poverty_rate=round(random.uniform(5, 50), 2),
        literacy_rate=round(random.uniform(75, 100), 2),
        unemployment_rate=round(random.uniform(2, 25), 2),
        healthcare_facilities=random.randint(1, 20),
        educational_institutions=random.randint(5, 50),
        industrial_units=random.randint(1, 15),
        average_income_per_person=round(random.uniform(150, 1000), 2),
        birth_rate=round(random.uniform(10, 40), 2),
        death_rate=round(random.uniform(5, 20), 2),
    )
    mfy.save()

models.MFY.objects.all()
print("Add MFYs")


# =======================================================================================================

for _ in range(1300):
    neighborhood = models.Neighborhood.objects.create(
        title=fake.word().capitalize(),
        elder=fake.name(),
        MFY=choice(models.MFY.objects.all()),
        area_km_kv=round(random.uniform(1, 50), 2),
        people=random.randint(500, 10000),
        population_density=round(random.uniform(100, 1500), 2),
        unemployment_rate=round(random.uniform(1, 20), 2),
        avg_income=round(random.uniform(500, 2000), 2),
        young_population=random.randint(100, 2000),
        working_population=random.randint(300, 5000),
        elderly_population=random.randint(100, 1500),
        education_high=random.randint(50, 1500),
        education_middle=random.randint(100, 2500),
        no_education=random.randint(100, 1000),
        
    )
    neighborhood.save()

models.Neighborhood.objects.all()
print("Add Neighborhoods")



# =======================================================================================================

for _ in range(2500):
    house = models.House.objects.create(
        house_boss=fake.name(),
        house_number=random.randint(1, 100),
        a_b=choice(['A', 'B']),
        neighborhood=choice(models.Neighborhood.objects.all()),
        status=choice(['POORER', 'MIDDLE', 'RICH']),
        people=random.randint(1, 10),
        area_kv_m=round(random.uniform(30, 500), 2),
        education_high=random.randint(0, 5),
        education_middle=random.randint(0, 5),
        no_education=random.randint(0, 5),
        electricity_available=choice([True, False]),
        water_available=choice([True, False]),
        gas_available=choice([True, False]),
    )
    house.save()

models.House.objects.all()
print("Add Houses")


# =======================================================================================================

for _ in range(4000):
    human = models.Human.objects.create(
        name=fake.first_name(),
        email=fake.email(),
        birth_date = fake.date_of_birth(),
        status=choice(['Kindergarten', 'Schoolboy', 'Student', 'Worker']),
        information=choice(['HIGH', 'MIDDLE', 'NO']),
        house=choice(models.House.objects.all()),
        working_hours_per_week=random.randint(0, 40),
        gender_distribution=choice(['MALE', 'FEMALE']),
        living_space_per_person=round(random.uniform(10, 50), 2),
    )
    human.save()

models.Human.objects.all()
print("Add Humans")



