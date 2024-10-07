from django.db import models
from django.contrib.auth.models import User
from localflavor.generic.models import IBANField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ibanformfieid = IBANField()
    icformfieid = models.CharField(max_length=100)

