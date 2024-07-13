from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listing/<str:title>", views.listing, name="listing"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("comment/<str:Comment_Listing>", views.comments, name="form"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("place_bid/<str:auction>", views.set_bid, name="place_bid"),
    path("add_to_watchlist/<str:auction>", views.add_to_watchlist, name="add_to_watchlist"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("close_auction/<str:auction>", views.close_auction, name="close_auction"),
    path("categories", views.Categories, name="categories"),
    path("category_list/<str:category>", views.category_list, name="category_list")
]
