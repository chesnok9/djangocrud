from django.contrib.auth.models import AbstractUser
from django.db import models
import random

class CustomUser(AbstractUser):
    # First/last name is not a global-friendly pattern
    # name = models.CharField(blank=True, max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    random_number = models.IntegerField(default=random.randint(1,101))

    def __str__(self):
        return self.email