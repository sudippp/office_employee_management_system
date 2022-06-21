from django.db import models

# Create your models here.
class Employee(models.Model):
    
    
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    employee_id = models.IntegerField(default=0)
    department = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    salary = models.IntegerField()
    bonus = models.IntegerField()
    phone_number = models.IntegerField()
    email_id = models.EmailField(max_length=100)
    joining_date = models.DateTimeField(auto_now_add=True)