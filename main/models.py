from django.db import models

class Question(models.Model):
  content = models.TextField()
  
  def get_absolute_url(self):
    return f'/question/{self.pk}/'

class Answer(models.Model):
  content = models.TextField()
  
  def get_absolute_url(self):
    return f'/answer/{self.pk}/'