from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=20)
    email=models.EmailField()
    phone_number=models.IntegerField()
    designation=models.CharField(max_length=20)
    salary=models.IntegerField()
    image=models.ImageField(upload_to='image')