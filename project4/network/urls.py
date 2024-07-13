
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name='profile'),
    path("following", views.following, name='following'),
    path("create_post", views.create_post, name='create_post'),
    path('addlike/<int:Post>', views.like, name='addlike'),
    path('profile/<str:person>', views.profile, name='profile'), 
    path('follow/<str:follower>/<str:followed>', views.follow, name='follow')
]
