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
