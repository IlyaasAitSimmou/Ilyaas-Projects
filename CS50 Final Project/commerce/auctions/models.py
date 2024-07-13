from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.categoryName}"


class Auction(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_items", blank=True, null=True)
    listing = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    imageUrl = models.CharField(max_length=1000)
    Activity = models.BooleanField(default=True)
    auction_lister = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_listings", blank=True, null=True)
    price = models.FloatField()
    watchlist = models.ManyToManyField(User ,related_name="watch_lists", blank=True, null=True)

    def __str__(self):
        return f"{self.listing} @ ${self.price}"

class Bid(models.Model):
    listing = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="bids")
    current_bid = models.PositiveIntegerField()
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids", blank=True, null=True)

    def __str__(self):
        return f"current bid: ${self.current_bid} of auction '{self.listing.listing}'"

class Comments(models.Model):
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    comment_listing = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(max_length=500)

    def __str__(self):
        return f"'{self.text}' commented by {self.commentor} on {self.comment_listing}"