from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views



urlpatterns = [

    path('', views.page_login),
    path('', views.profile),
    path('', views.profile_edit),

]

urlpatterns += staticfiles_urlpatterns()
