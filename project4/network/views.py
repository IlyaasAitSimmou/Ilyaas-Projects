from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime

from .forms import *
from .models import *


def index(request):
    all_posts = list(post.objects.all())
    postPages = []
    newList = []
    for i in range(len(all_posts)):
        newList.append(all_posts[i])
        if (i + 1)%10 == 0:
            postPages.append(newList)
            newList = []
    postPages.append(newList)
    return render(request, "network/index.html", {
        # 'posts': post.objects.all(),
        'postpages': postPages,
        'form': new_post
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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
    
def profile(request, person):
    all_posts = list(post.objects.filter(poster = User.objects.get(username=person)))
    postPages = []
    newList = []
    for i in range(len(all_posts)):
        newList.append(all_posts[i])
        if (len(newList))%10 == 0:
            postPages.append(newList)
            newList = []
    postPages.append(newList)
    return render(request, 'network/profile.html', {
        "person": User.objects.get(username=person),
        'postpages': postPages
        })

def following(request):
    all_posts = list(post.objects.filter(poster = User.objects.get(Followers=request.user)))
    postPages = []
    newList = []
    for i in range(len(all_posts)):
        newList.append(all_posts[i])
        if (len(newList))%10 == 0:
            postPages.append(newList)
            newList = []
    postPages.append(newList)
    return render(request, 'network/following.html', {
        'postpages': postPages
        })

def create_post(request):
    if request.method == 'POST':
        newPost = post(text=request.POST["text"], poster=request.user, date=datetime.today())
        newPost.save()
    return render(request, 'network/index.html', {
        'posts': post.objects.all(),
        'form': new_post
    })

def like(request, Post):
    if request.method == 'POST':
        if Like.objects.filter(liker=request.user, post=post.objects.get(pk=Post)).exists():
            Like.objects.get(liker=request.user, post=post.objects.get(pk=Post)).delete()
            return JsonResponse({"message": "Like removed!"})
        else:
            newlike = Like(post=post.objects.get(pk=Post), liker=request.user)
            newlike.save()
            return JsonResponse({"message": "Like added!"})
        
def follow(request, follower, followed):
    if request.method == 'POST':
        Followed = User.objects.get(username=followed)
        # if User.objects.get(username=followed).Followers_set.filter(username=follower):
        if User.objects.filter(username=followed, Followers=User.objects.get(username=follower)).exists():
            Followed.Followers.remove(User.objects.get(username=follower))
            return JsonResponse({"message": "Unfollowed"})
        else:
            Followed.Followers.add(User.objects.get(username=follower))
            Followed.save()
            return JsonResponse({"message": "Followed"})
