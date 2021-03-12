from django.db import models

# Create your models here.

class Product(models.Model): # only Model doesn't work
    title       = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price       = models.DecimalField(max_digits=7,decimal_places=2)
    summary     = models.TextField(blank=True, null=True)

class Employee(models.Model):
    emp_name       = models.TextField()
    emp_occupation = models.TextField()
    emp_id         = models.TextField()
    emp_salary     = models.TextField()
    emp_email      = models.EmailField(max_length=200)


class Anime(models.Model):
    anime_name       = models.TextField()
    anime_rating     = models.TextField()
    episodes_watched = models.TextField()

