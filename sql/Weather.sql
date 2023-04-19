Create table Weather (
    Location VARCHAR(20),
    DateStamp DATE,
    MaxTemp int,
    MinTemp int,
    Precipitation int,
    CONSTRAINT PK_WeatherEntry PRIMARY KEY (Location, DateStamp)
);