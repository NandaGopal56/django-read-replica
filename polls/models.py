from django.db import models

# Create your models here.
class Note(models.Model):
    body  = models.TextField(null=True, blank=True)
    updatedTime = models.DateTimeField(auto_now=True)
    createdTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]