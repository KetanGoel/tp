from django.db import models

# Create your models here.
class BlogDetails(models.Model):
    image = models.ImageField(upload_to='blog_images/')
    upload_date = models.DateField()
    title = models.CharField(max_length=200)
    content = models.TextField()


def __str__(self):
    return self.title