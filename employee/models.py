from django.conf import settings
from django.db import models
from django.utils import timezone

class Employee(models.Model):
    first_name = models.CharField ( max_length = 30)
    last_name = models.CharField ( max_length = 30 )
    email = models.CharField ( max_length = 40 )
    birth_date = models.DateField ( blank = True , null = True )

    def __str__(self):
        return self.first_name


