Create table Weather (
    Location VARCHAR(20),
    DateStamp DATE,
    MaxTemp float,
    MinTemp float,
    Precipitation float,
    CONSTRAINT PK_WeatherEntry PRIMARY KEY (Location, DateStamp)
);