from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)


class Superviser(models.Model):
    name = models.CharField(max_length=255)
    dempartement = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Memebership(models.Model):
    name = models.CharField(max_length=255)
    superviser = models.ForeignKey(Superviser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    membership = models.ForeignKey(Memebership, on_delete=models.CASCADE)
    superviser = models.ForeignKey(Superviser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
