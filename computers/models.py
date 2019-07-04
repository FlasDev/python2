from django.db import models

# Create your models here.
from django.urls import reverse


class Computer(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('computer-detail', args=[str(self.id)])


class OS(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)


class Producer(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
