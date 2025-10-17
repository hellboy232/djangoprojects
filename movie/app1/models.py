from django.db import models

# Create your models here.

class Moviedetail(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    language=models.CharField(max_length=20)
    year=models.IntegerField()
    director=models.CharField(max_length=20)
    image=models.ImageField(upload_to="images")
