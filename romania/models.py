from django.db import models

# Create your models here.
from django.utils import timezone


class County(models.Model):
    name = models.CharField(max_length=64)
    county_short_name = models.CharField(max_length=2)
    county_code = models.IntegerField(null=True)


class DailyReport(models.Model):
    date = models.DateField(default=timezone.now, unique=True)
    cases = models.IntegerField(null=True, blank=True)
    tests = models.IntegerField(null=True, blank=True)
    tested_people = models.IntegerField(null=True, blank=True)
    dead = models.IntegerField(null=True, blank=True)
    icu = models.IntegerField(null=True, blank=True)
    critical = models.IntegerField(null=True, blank=True)
    recovered = models.IntegerField(null=True, blank=True)
    time_updated = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)
    county_data = models.ManyToManyField(County, through='CountyData')


    def __str__(self):
        return self.date.isoformat()


class CountyData(models.Model):
    report = models.ForeignKey(DailyReport, on_delete=models.CASCADE)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    cases = models.IntegerField()