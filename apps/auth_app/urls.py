from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="account-login"),
    path("register", views.register, name="account-register")
]
