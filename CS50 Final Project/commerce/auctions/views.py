from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


def index(request):
    return render(request, "auctions/index.html",{
        "auctions": Auction.objects.all()        
    })

def listing(request, title):
    if Auction.objects.get(listing=title).bids.first().bidder == request.user:
        return render(request, "auctions/winner.html",{
            "winner": f"congratulations {request.user.username}! You have won the following the auction, {title}!"
    })
    is_auction_lister = request.user == Auction.objects.get(listing=title).auction_lister
    return render(request, "auctions/listing.html",{
        "auction": Auction.objects.get(listing=title),
        "form": comment(),
        "Comment_Listing": title,
        "Comments":Comments.objects.filter(comment_listing=Auction.objects.get(listing=title)),
        "is_auction_lister": is_auction_lister,
        "place_bid": PlaceBid
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    
@login_required
def comments(request, Comment_Listing):
    if request.method == 'POST':
        com = Comments(commentor=request.user, comment_listing=Auction.objects.get(listing=Comment_Listing), text = request.POST['comment'])
        com.save()
    return listing(request, Comment_Listing)

@login_required
def create_listing(request):
    if request.method == 'GET':
        return render(request, "auctions/create_listing.html", {
            "form": NewListing
        })
    else:
        new_listing = Auction(listing=request.POST['listing'], category=Category.objects.get(categoryName=request.POST['category']), description=request.POST['description'], imageUrl=request.POST['imageUrl'], auction_lister=request.user, price=request.POST['price'])
        new_listing.save()
        return listing(request, request.POST['listing'])

@login_required
def set_bid(request, auction):
    if request.method == 'POST':
        try:
            if Bid.objects.get(listing=Auction.objects.get(listing=auction)):
                New_bid = Bid.objects.get(listing=Auction.objects.get(listing=auction))
                if int(request.POST['bid']) > New_bid.current_bid:
                    New_bid.current_bid = int(request.POST['bid'])
                    New_bid.bidder = request.user
        except:
            if int(request.POST['bid']) > Auction.objects.get(listing=auction).price:
                New_bid = Bid(listing=Auction.objects.get(listing=auction), current_bid=int(request.POST['bid']), bidder = request.user)
        New_bid.save()
    return listing(request, auction)

@login_required
def watchlist(request):
    return render(request, "auctions/watchlist.html", {
            "watchlist": request.user.watch_lists.all()
        })

@login_required
def add_to_watchlist(request, auction):
    if request.method == 'POST':
        Watchlist_auction = Auction.objects.get(listing=auction)
        Watchlist_auction.watchlist.add(request.user)
    return watchlist(request)

def close_auction(request, auction):
    if request.method == 'POST':
        closed_auction = Auction.objects.get(listing=auction)
        closed_auction.Activity = False
        closed_auction.save()
    return index(request)

def Categories(request):
    return render(request, "auctions/categories.html", {
        "categories": Category.objects.all()
    })

def category_list(request, category):
    return render(request, "auctions/category_list.html", {
        "category": category,
        "auctions": Auction.objects.filter(category=Category.objects.get(categoryName=category))
    })




