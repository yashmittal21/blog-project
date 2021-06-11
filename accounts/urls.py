from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("register",views.register,name = 'register'),
    path("login",views.login_view,name="login"),
    path("logout",views.logout_view,name="logout")
] 