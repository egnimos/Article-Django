from django.db import models

# Create your models here.
class Article(models.Model):
    pass


class User(models.Model):
    image = models.ImageField(upload_to="profile_pics")
    name = models.CharField(max_length=100)
    email_address = models.EmailField()
