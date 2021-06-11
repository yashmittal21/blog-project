
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home,name="home"),
    url(r'^create$',views.create_article,name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.detail,name="detail"),
] 