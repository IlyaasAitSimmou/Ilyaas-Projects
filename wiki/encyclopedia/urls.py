from django.urls import path

from . import views


app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.getTitle, name="title"),
    path("searchresults/", views.Search, name="searchresults"),
    path("newpage/", views.page_creator, name="newpage"),
    path("random/", views.random, name="random"),
    path("editpage/<str:title>", views.edit_page, name="editpage"),
    path("savepage/<str:title>", views.save_page, name="savepage")
]
