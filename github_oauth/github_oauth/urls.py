from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from home import views


urlpatterns = [
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),  # <--
]


urlpatterns += [
    path('', views.home, name='home'),
    path('repos/', views.repos, name='repos'),
    path('organizations/', views.organizations, name='organizations'),
]