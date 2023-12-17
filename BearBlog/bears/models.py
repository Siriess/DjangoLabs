from django.db import models

class FeedBacks(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    text = models.TextField()
    verified = models.BooleanField(default=False)