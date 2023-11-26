import mysql.connector
from datetime import date
import random

# Connect to MySQL server
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'spacedb',
    'port': 3307,
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor(dictionary=True)

# Function to generate a random ID
def generate_random_id():
    return str(random.randint(100000, 999999))

# Function to insert data into Stars table
def insert_star(name, spectral_type, temperature, luminosity):
    star_id = generate_random_id()
    cursor.execute("INSERT INTO Star (StarID, Name, SpectralType, Temperature, Luminosity) VALUES (%s, %s, %s, %s, %s)",
                   (star_id, name, spectral_type, temperature, luminosity))
    conn.commit()
    return star_id

# Function to insert data into SolarSystems table
def insert_solar_system(name, age, star_id):
    solar_system_id = generate_random_id()
    cursor.execute("INSERT INTO SolarSystems (SolarSystemID, Name, Age, StarID) VALUES (%s, %s, %s, %s)", (solar_system_id, name, age, star_id))
    conn.commit()
    return solar_system_id

# Function to insert data into Planets table
def insert_planet(name, mass, radius, age, discovery_date, solar_system_id):
    planet_id = generate_random_id()
    cursor.execute("INSERT INTO Planet (PlanetID, Name, Mass, Radius, Age, DiscoveryDate, SolarSystemID) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (planet_id, name, mass, radius, age, discovery_date, solar_system_id))
    conn.commit()
    return planet_id

# Function to insert data into Moons table
def insert_moon(name, mass, radius, age, discovery_date, planet_id):
    moon_id = generate_random_id()
    cursor.execute("INSERT INTO Moon (MoonID, Name, Mass, Radius, Age, DiscoveryDate, PlanetID) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (moon_id, name, mass, radius, age, discovery_date, planet_id))
    conn.commit()

# Insert Sun into Stars table
sun_id = insert_star("Sun", "G-type", 5778, 1)

# Insert Solar System
solar_system_id = insert_solar_system("Our Solar System", 4.6, sun_id)

# Insert Planets of our Solar System
mercury_id = insert_planet("Mercury", 0.330, 2439.7, 4.5, date(1631, 12, 27), solar_system_id)
venus_id = insert_planet("Venus", 4.87, 6051.8, 4.5, date(1761, 6, 1), solar_system_id)
earth_id = insert_planet("Earth", 5.97, 6371, 4.5, date(1776, 7, 4), solar_system_id)
mars_id = insert_planet("Mars", 0.64171, 3389.5, 4.6, date(1659, 12, 27), solar_system_id)
jupiter_id = insert_planet("Jupiter", 1898, 69911, 4.6, date(1610, 1, 7), solar_system_id)
saturn_id = insert_planet("Saturn", 568, 58232, 4.6, date(1610, 7, 25), solar_system_id)
uranus_id = insert_planet("Uranus", 86.8, 25362, 4.5, date(1781, 3, 13), solar_system_id)
neptune_id = insert_planet("Neptune", 102, 24622, 4.5, date(1846, 9, 23), solar_system_id)

# Insert Moons for Earth
insert_moon("Moon", 0.073, 1737, 4.5, date(1776, 7, 4), earth_id)

# Insert Moons for Mars
insert_moon("Phobos", 1.08e-8, 11.1, 4.6, date(1877, 8, 18), mars_id)
insert_moon("Deimos", 2.4e-9, 6.2, 4.6, date(1877, 8, 12), mars_id)

# Insert Moons for Jupiter
insert_moon("Io", 893.3, 1821.6, 4.6, date(1610, 1, 8), jupiter_id)
insert_moon("Europa", 480.0, 1560.8, 4.6, date(1610, 1, 8), jupiter_id)
insert_moon("Ganymede", 1481, 2634.1, 4.6, date(1610, 1, 7), jupiter_id)
insert_moon("Callisto", 1076, 2410.3, 4.6, date(1610, 1, 7), jupiter_id)

# Insert Moons for Saturn
insert_moon("Titan", 13455, 2574.7, 4.6, date(1655, 3, 25), saturn_id)
insert_moon("Enceladus", 1.08e-8, 252.3, 4.6, date(1789, 8, 28), saturn_id)

# Insert Moons for Uranus
insert_moon("Titania", 3.4e-8, 788.9, 4.5, date(1787, 1, 11), uranus_id)
insert_moon("Oberon", 2.9e-8, 761.4, 4.5, date(1787, 1, 11), uranus_id)

# Insert Moons for Neptune
insert_moon("Triton", 2140, 1353.4, 4.5, date(1846, 10, 10), neptune_id)

# Close the connection
cursor.close()
conn.close()
