"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from user import views as user_views
from Proj_dir import views as prof_views
from django.contrib.auth.decorators import login_required, permission_required

from blog.views import (
NewsListView,
PostCreateView,
PostDetailView,
PostUpdateView,
PostDeleteView,

)

urlpatterns = [
    path('', prof_views.index, name='index'),
    path('index/', prof_views.index, name='index'),
    path('about/', prof_views.about, name='about'),
    path('contact/', prof_views.contact, name='contact'),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('reset/', auth_views.LoginView.as_view(template_name='user/password_reset_form.html'), name='reset'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('edit_profile/', user_views.profile_edit, name='profile_edit'),
    path('news_post/', NewsListView.as_view(), name='news_post'),
    path('create_post/', PostCreateView.as_view(), name='create_post'),
    path('post/<pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<pk>/update',  PostUpdateView.as_view(), name='update_post'),
    path('post/<pk>/delete', PostDeleteView.as_view(), name='delete_post'),
    path('profile/posts', login_required(NewsListView.as_view()), name='posts')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
