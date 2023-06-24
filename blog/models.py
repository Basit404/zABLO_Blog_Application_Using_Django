from django.db import models
from tinymce.models import HTMLField

# Create your models here.

# model for post
class Blog(models.Model):
    s_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = HTMLField()
    slug = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# model for feedback
class Feedback(models.Model):
    s_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    desc = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
