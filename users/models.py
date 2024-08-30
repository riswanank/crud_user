from django.db import models

# Create your models here.

class User(models.Model):
  id= models.IntegerField(primary_key=True)
  username = models.CharField(max_length=255)
  password = models.CharField(max_length=20)
  active=models.BooleanField()

  def __str__(self):
    return f" {self.id}{self.username} {self.password} {self.active}"