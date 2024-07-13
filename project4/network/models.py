from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    Followers = models.ManyToManyField("self", related_name="followers", blank=True, null=True)
    pass

class post(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_listings")
    text = models.CharField(max_length=300)
    date = models.DateTimeField()

class Like(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE, related_name="likes")
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")

class Comments(models.Model):
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    comment_post = models.ForeignKey(post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(max_length=500)



