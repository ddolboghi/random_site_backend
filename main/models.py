from django.db import models
from django.contrib.postgres.fields import ArrayField

class Alldata(models.Model):
  is_choice = models.BooleanField(default=True)
  question = models.TextField()
  answer1 = models.TextField()
  answer2 = models.TextField()
  answer3 = models.TextField()
  
  def get_absolute_url(self):
    return f'/Alldata/{self.pk}/'
  
class Result(models.Model):
  content = models.TextField()
  
  def get_absolute_url(self):
    return f'/Result/{self.pk}/'
 