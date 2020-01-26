from django.db import models
from passlib.hash import pbkdf2_sha256

class account(models.Model) :
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    passwd = models.CharField(max_length = 300)

    def verify_password(self,passwd):
      return pbkdf2_sha256.verify(passwd,self.passwd)

