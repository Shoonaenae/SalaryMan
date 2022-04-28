from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.nPANN
class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=20)

    class meta:
        db_table = 'tblCity'

class Employer(models.Model):
    employer_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)

    class meta:
        db_table = 'tblEmployer'

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    age = models.IntegerField()
    contact_num = models.CharField(max_length=20)
    year_hired = models.DateTimeField(blank=True, null=True)   

    class meta:
        db_table = 'tblEmployee'

class Salary(models.Model):
    salary_id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField()