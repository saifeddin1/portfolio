from django.db import models

class Job(models.Model):
    #images
    image = models.ImageField(upload_to = 'images/')
    #summary
    summary = models.CharField(max_length=200)
    title = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.title  