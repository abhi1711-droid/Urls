from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views
from users.views import SignUpView

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.listall, name="listall"),
    path('search/searchlink', views.searchlink, name="searchlink"),
    path('search/', views.search, name="search"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path("logout_user", views.logout_user, name="logout_user"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
