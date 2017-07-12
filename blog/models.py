from django.db import models
from django.utils import timezone

class Post(models.Model): #defines the model- it's an object. Post:name of model.
    author = models.ForeignKey('auth.User') #link to another model
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

def publish(self): #the publishing method
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title

# Create your models here.
