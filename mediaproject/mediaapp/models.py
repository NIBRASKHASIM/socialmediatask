from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    post_desc=models.CharField(max_length=200)
    date_created=models.DateField(auto_now=True)
    image=models.ImageField(upload_to='Images',default="Image/None/NoImg.jpg")


class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    comment_date = models.DateTimeField(default=timezone.now)


class Like(models.Model):

    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
