from django.db import models

# Create your models here.


class User(models.Model):
    url = models.URLField()
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    groups = models.ForeignKey('Group', on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Group(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
