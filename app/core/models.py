from django.db import models

PERIOD_TYPE = (
    ('Monthly', 'Monthly'),
    ('Quartely', 'Quartely')
)

class OrgUnits(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    us_name = models.CharField(max_length=255)
    province_name = models.CharField(max_length=255)
    district_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.us_name

class DataElement(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
class Indicator(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    numerator_names = models.TextField()
    numerator = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class Program(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
class DataValueSet(models.Model):
    data_element = models.ForeignKey(DataElement, on_delete=models.CASCADE)
    period = models.CharField(max_length=255)
    orgunit = models.ForeignKey(OrgUnits, on_delete=models.CASCADE)
    categoryOptionCombo = models.CharField(max_length=255, null=True, blank=True)
    attributeOptionCombo = models.CharField(max_length=255, null=True, blank=True)
    value = models.IntegerField(null=True)
    period_type = models.CharField(max_length=10, choices=PERIOD_TYPE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.data_element.name