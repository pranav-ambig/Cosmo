from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Function to generate a random date within a specific range in the format 'YYYY-MM-DD'
def random_date(start_date, end_date):
    random_days = random.randint(0, (end_date - start_date).days)
    return (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

# Function to generate synthetic data for the SolarSystems table
def generate_solar_systems_data():
    solar_systems_data = []
    for _ in range(5, 16):
        solar_system = {
            'SolarSystemID': fake.unique.random_number(),
            'Name': fake.unique.word(),
            'Age': random.randint(1, 10**9),
            'StarID': fake.unique.random_number(),
        }
        solar_systems_data.append(solar_system)
    return solar_systems_data

# Function to generate synthetic data for the Stars table
def generate_stars_data(solar_systems_data):
    stars_data = []
    for solar_system in solar_systems_data:
        star = {
            'StarID': solar_system['StarID'],
            'Name': fake.unique.word(),
            'SpectralType': fake.random_element(elements=('O', 'B', 'A', 'F', 'G', 'K', 'M')),
            'Temperature': random.randint(2000, 50000),
            'Luminosity': fake.pydecimal(left_digits=2, right_digits=2, positive=True),
            'SolarSystemID': solar_system['SolarSystemID'],
        }
        stars_data.append(star)
    return stars_data

# Function to generate synthetic data for the Galaxies table
def generate_galaxies_data(solar_systems_data):
    galaxies_data = []
    for solar_system in solar_systems_data:
        galaxy = {
            'GalaxyID': fake.unique.random_number(),
            'Name': fake.unique.word(),
            'Type': fake.random_element(elements=('Spiral', 'Elliptical', 'Irregular')),
            'Size': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
            'Age': random.randint(1, 10**9),
            'SolarSystemID': solar_system['SolarSystemID'],
        }
        galaxies_data.append(galaxy)
    return galaxies_data

# Function to generate synthetic data for the Planets table
def generate_planets_data(solar_systems_data):
    planets_data = []
    for solar_system in solar_systems_data:
        for _ in range(random.randint(3, 10)):
            planet = {
                'PlanetID': fake.unique.random_number(),
                'Name': fake.unique.word(),
                'Mass': fake.pydecimal(left_digits=10, right_digits=2, positive=True),
                'Radius': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
                'Age': random.randint(1, 10**9),
                'DiscoveryDate': random_date(datetime(2000, 1, 1), datetime(2023, 1, 1)),
                'MoonID': fake.unique.random_number(),
                'SolarSystemID': solar_system['SolarSystemID'],
            }
            planets_data.append(planet)
    return planets_data

# Function to generate synthetic data for the Moons table
def generate_moons_data(planets_data):
    moons_data = []
    for planet in planets_data:
        moon = {
            'MoonID': fake.unique.random_number(),
            'Name': fake.unique.word(),
            'Mass': fake.pydecimal(left_digits=8, right_digits=2, positive=True),
            'Radius': fake.pydecimal(left_digits=4, right_digits=2, positive=True),
            'Age': random.randint(1, 10**9),
            'DiscoveryDate': random_date(datetime(2000, 1, 1), datetime(2023, 1, 1)),
            'PlanetID': planet['PlanetID'],
        }
        moons_data.append(moon)
    return moons_data

# Function to generate synthetic data for the Nebulae table
def generate_nebulae_data(galaxies_data):
    nebulae_data = []
    for galaxy in galaxies_data:
        nebula = {
            'NebulaID': fake.unique.random_number(),
            'Name': fake.unique.word(),
            'Type': fake.random_element(elements=('Emission', 'Reflection', 'Dark')),
            'Size': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
            'Location': fake.unique.word(),
            'GalaxyID': galaxy['GalaxyID'],
        }
        nebulae_data.append(nebula)
    return nebulae_data

# Function to generate synthetic data for the BlackHole table
def generate_black_holes_data(galaxies_data):
    black_holes_data = []
    for galaxy in galaxies_data:
        black_hole = {
            'BlackHoleID': fake.unique.random_number(),
            'Name': fake.unique.word(),
            'Mass': fake.pydecimal(left_digits=10, right_digits=2, positive=True),
            'Radius': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
            'Age': random.randint(1, 10**9),
            'DiscoveryDate': random_date(datetime(2000, 1, 1), datetime(2023, 1, 1)),
            'GalaxyID': galaxy['GalaxyID'],
        }
        black_holes_data.append(black_hole)
    return black_holes_data

# Function to generate synthetic data for the Asteroids table
def generate_asteroids_data(solar_systems_data):
    asteroids_data = []
    for solar_system in solar_systems_data:
        asteroid = {
            'AsteroidID': fake.unique.random_number(),
            'Name': fake.unique.word(),
            'Mass': fake.pydecimal(left_digits=8, right_digits=2, positive=True),
            'Radius': fake.pydecimal(left_digits=4, right_digits=2, positive=True),
            'Age': random.randint(1, 10**9),
            'DiscoveryDate': random_date(datetime(2000, 1, 1), datetime(2023, 1, 1)),
            'SolarSystemID': solar_system['SolarSystemID'],
            'GalaxyID': fake.unique.random_number(),
        }
        asteroids_data.append(asteroid)
    return asteroids_data

# Function to generate synthetic data for the LocalGroup table
def generate_local_groups_data(galaxies_data):
    local_groups_data = []
    for galaxy in galaxies_data:
        local_group = {
            'ClusterID': fake.unique.random_number(),
            'Name': fake.unique.word(),
            'Type': fake.random_element(elements=('Small', 'Medium', 'Large')),
            'Size': fake.pydecimal(left_digits=5, right_digits=2, positive=True),
            'Age': random.randint(1, 10**9),
            'GalaxyID': galaxy['GalaxyID'],
        }
        local_groups_data.append(local_group)
    return local_groups_data

# Function to insert data into the database tables
def insert_data(connection, cursor, table_name, data):
    for record in data:
        columns = ', '.join(record.keys())
        values = ', '.join([f"'{value}'" if isinstance(value, str) else str(value) for value in record.values()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
        try:
            cursor.execute(query)
        except Exception as e:
            print(f"Error inserting data into {table_name}: {e}")
    connection.commit()


# Connect to your database (replace 'your_database' and 'your_user' with your actual database and user)
# Use the appropriate database connection library (e.g., pymysql, psycopg2, sqlite3) based on your database
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'spacedb',
    'port': 3307,
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor(dictionary=True)

def getfromdb():
    cursor.execute('SELECT * from solarsystems')
    ret = []
    for i in cursor:
        ret.append(i)
    return ret

# Generate and insert data into tables
# solar_systems_data = generate_solar_systems_data()
solar_systems_data = getfromdb()
insert_data(connection, cursor, 'SolarSystems', solar_systems_data)

# stars_data = generate_stars_data(solar_systems_data)
# insert_data(connection, cursor, 'Star', stars_data)

# galaxies_data = generate_galaxies_data(solar_systems_data)
# insert_data(connection, cursor, 'Galaxy', galaxies_data)

planets_data = generate_planets_data(solar_systems_data)
insert_data(connection, cursor, 'Planet', planets_data)

# moons_data = generate_moons_data(planets_data)
# insert_data(connection, cursor, 'Moon', moons_data)

# nebulae_data = generate_nebulae_data(galaxies_data)
# insert_data(connection, cursor, 'Nebula', nebulae_data)

# black_holes_data = generate_black_holes_data(galaxies_data)
# insert_data(connection, cursor, 'BlackHole', black_holes_data)

# asteroids_data = generate_asteroids_data(solar_systems_data)
# insert_data(connection, cursor, 'Asteroid', asteroids_data)

# local_groups_data = generate_local_groups_data(galaxies_data)
# insert_data(connection, cursor, 'Cluster', local_groups_data)

# Close the database connection

getfromdb()
connection.close()
