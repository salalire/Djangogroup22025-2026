from django.db import models

class Note(models.Model):
    title=models.CharField(max_length=100)
    messages=models.TextField()
