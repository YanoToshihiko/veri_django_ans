from django.db import models

# Create your models here.


class Employee(models.Model):
    no = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    # address_cd = models.IntegerField(null=True)

    def __str__(self):
        return self.name
