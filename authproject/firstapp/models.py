from django.db import models


class UserRegistrationModel(models.Model):
    username = models.CharField( max_length = 150)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 40)