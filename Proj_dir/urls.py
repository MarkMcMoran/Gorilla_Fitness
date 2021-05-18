from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url('', views.index, name="index"),
    url('', views.contact, name="contact"),
    url('', views.about, name="about")
]

urlpatterns += staticfiles_urlpatterns()