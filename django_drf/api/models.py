from django.db import models

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.title


class Article(models.Model):
    title = models.CharField(max_length=100)
    author =models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title