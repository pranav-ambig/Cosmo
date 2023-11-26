-- Get details of a planet
SELECT *
FROM Planet
WHERE Name = 'Earth';

--CRUD

--Create
INSERT INTO Planet (Name, Mass, Radius, Age, DiscoveryDate, SolarSystemID)
VALUES ('NewPlanet', 10.5, 15.2, 500, '2023-11-24', 1);

--Read
SELECT Moon.Name, Moon.Mass, Moon.Radius
FROM Moon
JOIN Planet ON Moon.PlanetID = Planet.PlanetID
WHERE Planet.Name = 'Jupiter';

--Update
UPDATE Star
SET Temperature = 6000
WHERE StarID = 1;

--Delete
DELETE FROM Asteroid
WHERE AsteroidID = 1;


-- Explore moons of a particular planet:
SELECT Moon.Name, Moon.Mass, Moon.Radius
FROM Moon
JOIN Planet ON Moon.PlanetID = Planet.PlanetID
WHERE Planet.Name = 'Jupiter';

-- Discover stars in a solar system:
SELECT Star.Name, Star.SpectralType, Star.Temperature, Star.Luminosity
FROM Star
JOIN SolarSystem ON Star.SolarSystemID = SolarSystem.SolarSystemID
WHERE SolarSystem.Name = 'Our Solar System';

-- Find stars in each solar system with their spectral type:
SELECT SolarSystem.Name AS SolarSystemName, Star.Name AS StarName, Star.SpectralType
FROM SolarSystem
JOIN Star ON SolarSystem.SolarSystemID = Star.SolarSystemID;

-- Find galaxies with their black holes and associated solar systems:
SELECT Galaxy.Name AS GalaxyName, BlackHole.Name AS BlackHoleName, SolarSystem.Name AS SolarSystemName
FROM Galaxy
LEFT JOIN BlackHole ON Galaxy.GalaxyID = BlackHole.GalaxyID
LEFT JOIN SolarSystem ON Galaxy.SolarSystemID = SolarSystem.SolarSystemID;

-- Find the oldest planet in each solar system-- 
SELECT SolarSystem.Name AS SolarSystemName, Planet.Name AS OldestPlanet
FROM SolarSystem
JOIN Planet ON SolarSystem.SolarSystemID = Planet.SolarSystemID
WHERE Planet.Age = (SELECT MAX(Age) FROM Planet WHERE SolarSystemID = SolarSystem.SolarSystemID);

-- List moons that are larger than the average moon radius:
SELECT Name, Radius
FROM Moon
WHERE Radius > (SELECT AVG(Radius) FROM Moon);

-- Find galaxies with the largest average black hole mass:
SELECT Galaxy.Name AS GalaxyName, AVG(BlackHole.Mass) AS AvgBlackHoleMass
FROM Galaxy
LEFT JOIN BlackHole ON Galaxy.GalaxyID = BlackHole.GalaxyID
GROUP BY Galaxy.GalaxyID
HAVING AVG(BlackHole.Mass) = (SELECT MAX(AvgMass) FROM (SELECT AVG(Mass) AS AvgMass FROM BlackHole GROUP BY GalaxyID) AS AvgMassPerGalaxy);


-- Create Trigger to Update Total Number of Planets in a Solar System
DELIMITER //
-- Create Trigger to Update Total Number of Planets in a Solar System
CREATE TRIGGER UpdateSolarSystemTotalPlanets
AFTER INSERT ON Planet
FOR EACH ROW
BEGIN
    -- Update the total number of planets in the solar system
    UPDATE SolarSystem
    SET TotalPlanets = (
        SELECT COUNT(*)
        FROM Planet
        WHERE SolarSystemID = NEW.SolarSystemID
    )
    WHERE SolarSystemID = NEW.SolarSystemID;
END//
DELIMITER ;

-- Create Function to Calculate Average Mass of Planets in a Solar System
DELIMITER //
CREATE FUNCTION CalculateAverageMass(solarSystemID INT)
RETURNS DECIMAL(18, 2)
BEGIN
    DECLARE avgMass DECIMAL(18, 2);
    
    SELECT AVG(Mass) INTO avgMass
    FROM Planet
    WHERE SolarSystemID = solarSystemID;

    RETURN avgMass;
END //
DELIMITER ;


--Nested query that retrieves information about planets 
--in solar systems that belong to a specific galaxy
SELECT *
FROM Planet
WHERE SolarSystemID IN (
    SELECT SolarSystemID
    FROM SolarSystem
    WHERE Solarsystem.GalaxyID = (
        SELECT GalaxyID
        FROM Galaxy
        WHERE Name = 'Milky Way'
    )
);

-- Procedure to get all planets of a solarsystem
DELIMITER //

CREATE PROCEDURE GetPlanetsInSolarSystem(IN solarSystemID INT)
BEGIN
    SELECT Name, Mass, Radius
    FROM Planet
    WHERE SolarSystemID = solarSystemID;
END //

DELIMITER ;

--query to find cluster names of all planets

SELECT
    Planet.Name AS PlanetName,
    Cluster.Name AS ClusterName
FROM
    Cluster
JOIN
    Galaxy ON Cluster.GalaxyID = Galaxy.GalaxyID
JOIN
    SolarSystems ON Galaxy.GalaxyID = SolarSystems.GalaxyID
JOIN
    Planet ON SolarSystems.SolarSystemID = Planet.SolarSystemID;
