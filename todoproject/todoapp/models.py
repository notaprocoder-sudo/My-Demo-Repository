from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=150)
    prio = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.task