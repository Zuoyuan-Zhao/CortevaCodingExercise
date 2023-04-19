from django.db import models


class Weather(models.Model):
    Location = models.CharField(max_length=20, primary_key=True)
    DateStamp = models.DateField()
    MaxTemp = models.FloatField()
    MinTemp = models.FloatField()
    Precipitation = models.FloatField()

    class Meta:
        db_table = 'Weather'
        unique_together = (('Location', 'DateStamp'))


class WeatherStats(models.Model):
    Location = models.CharField(max_length=20, primary_key=True)
    Year = models.IntegerField()
    MaxTempAvg = models.FloatField()
    MinTempAvg = models.FloatField()
    TotalPrecipitation = models.FloatField()

    class Meta:
        db_table = 'WeatherStats'
        unique_together = (('Location', 'Year'))

