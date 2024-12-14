from django.urls import path

from . import views

app_name = "Pages"

urlpatterns = [
    path("", views.HomePage.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("rules/", views.RulesView.as_view(), name="rules"),
]
