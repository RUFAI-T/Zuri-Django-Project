from django.urls import path
from . import views


urlpatterns = [
    path("", views.ListArtisteApi.as_view(), name="home"),
    path("create/", views.CreateArtisteApi.as_view(), name="create"),
    path("", views.ListSongApi.as_view(), name="home"),
    path("createsong/", views.CreateSongApi.as_view(), name="create"),
    path("", views.ListLyricApi.as_view(), name="home"),
    path("createlyric/", views.CreateLyricApi.as_view(), name="create"),
    path('home.html', views.home, name="home"),
    path('about.html', views.about, name="about"),

]