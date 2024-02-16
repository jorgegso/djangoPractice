from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=200)


class Task():
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
