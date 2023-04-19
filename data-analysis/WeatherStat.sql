Create table WeatherStats (
    Location VARCHAR(20),
    Year int,
    MaxTempAvg float,
    MinTempAvg float,
    TotalPrecipitation float,
    CONSTRAINT PK_WeatherEntry PRIMARY KEY (Location, Year)
);


CREATE PROCEDURE `calculate_weather_stats`()
BEGIN
    INSERT INTO WeatherStats (Location, Year, MaxTempAvg, MinTempAvg, TotalPrecipitation)
    SELECT Location, YEAR(DateStamp) AS Year, AVG(MaxTemp) AS MaxTempAvg, AVG(MinTemp) AS MinTempAvg, SUM(Precipitation) AS TotalPrecipitation
    FROM Weather
    GROUP BY Location, YEAR(DateStamp)
    ON DUPLICATE KEY UPDATE
    MaxTempAvg = IFNULL(VALUES(MaxTempAvg), MaxTempAvg),
    MinTempAvg = IFNULL(VALUES(MinTempAvg), MinTempAvg),
    TotalPrecipitation = IFNULL(VALUES(TotalPrecipitation), TotalPrecipitation);
END
