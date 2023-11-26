-- Solar Systems Table
CREATE TABLE SolarSystems (
    SolarSystemID INT PRIMARY KEY,
    Name VARCHAR(255),
    Age INT,
    StarID INT
);

-- Planets Table
CREATE TABLE Planet (
    PlanetID INT PRIMARY KEY,
    Name VARCHAR(255),
    Mass DECIMAL(18, 2),
    Radius DECIMAL(18, 2),
    Age INT,
    DiscoveryDate DATE,
    MoonID INT,
    SolarSystemID INT,
    FOREIGN KEY (SolarSystemID) REFERENCES SolarSystems(SolarSystemID)
);

-- Moons Table
CREATE TABLE Moon (
    MoonID INT PRIMARY KEY,
    Name VARCHAR(255),
    Mass DECIMAL(18, 2),
    Radius DECIMAL(18, 2),
    Age INT,
    DiscoveryDate DATE,
    PlanetID INT,
    FOREIGN KEY (PlanetID) REFERENCES Planet(PlanetID)
);

-- Stars Table
CREATE TABLE Star (
    StarID INT PRIMARY KEY,
    Name VARCHAR(255),
    SpectralType VARCHAR(10),
    Temperature INT,
    Luminosity DECIMAL(18, 2),
    SolarSystemID INT,
    FOREIGN KEY (SolarSystemID) REFERENCES SolarSystems(SolarSystemID)
);

-- Asteroids Table
CREATE TABLE Asteroid (
    AsteroidID INT PRIMARY KEY,
    Name VARCHAR(255),
    Mass DECIMAL(18, 2),
    Radius DECIMAL(18, 2),
    Age INT,
    DiscoveryDate DATE,
    SolarSystemID INT,
    GalaxyID INT,
    FOREIGN KEY (SolarSystemID) REFERENCES SolarSystems(SolarSystemID)
);

-- Nebulae Table
CREATE TABLE Nebula (
    NebulaID INT PRIMARY KEY,
    Name VARCHAR(255),
    Type VARCHAR(50),
    Size DECIMAL(18, 2),
    Location VARCHAR(255),
    GalaxyID INT
    -- FOREIGN KEY (GalaxyID) REFERENCES Galaxy(GalaxyID)
);

-- Galaxies Table
CREATE TABLE Galaxy (
    GalaxyID INT PRIMARY KEY,
    Name VARCHAR(255),
    Type VARCHAR(50),
    Size DECIMAL(18, 2),
    Age INT,
    SolarSystemID INT,
    FOREIGN KEY (SolarSystemID) REFERENCES SolarSystems(SolarSystemID)
);

-- BlackHole Table
CREATE TABLE BlackHole (
    BlackHoleID INT PRIMARY KEY,
    Name VARCHAR(255),
    Mass DECIMAL(18, 2),
    Radius DECIMAL(18, 2),
    Age INT,
    DiscoveryDate DATE,
    GalaxyID INT,
    FOREIGN KEY (GalaxyID) REFERENCES Galaxy(GalaxyID)
);

-- LocalGroup Table
CREATE TABLE Cluster (
    ClusterID INT PRIMARY KEY,
    Name VARCHAR(255),
    Type VARCHAR(50),
    Size DECIMAL(18, 2),
    Age INT,
    GalaxyID INT,
    FOREIGN KEY (GalaxyID) REFERENCES Galaxy(GalaxyID)
);

