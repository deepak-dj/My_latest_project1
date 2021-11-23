from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/',null=True)

    def __str__(self):
        return self.name
