from django.db import models


class account(models.Model) :
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    passwd = models.CharField(max_length = 300)


