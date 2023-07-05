from django.db import models
from accounts.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
