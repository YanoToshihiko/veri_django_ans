from django.db import models

# Create your models here.


def validate_no(value):
    if not ( 1000 <= value <= 9999) :
        raise ValidationError(('%(value)s is not a valid number'),
            params={'value': value},
        )
    return value


class Employee(models.Model):
    no = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    # address_cd = models.IntegerField(null=True)

    def __str__(self):
        return self.name
