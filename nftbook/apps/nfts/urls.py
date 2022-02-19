from . import views
from django.urls import path

app_name = "nfts"
urlpatterns = [
    path("", views.HomePageView.as_view(), name="home")
]
