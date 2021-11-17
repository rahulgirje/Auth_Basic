from django.urls import path
from .views import registerView,home,loginView,logoutView

urlpatterns = [
    path('',home),
    path('login/',loginView, name='login'),
    path('logout/',logoutView, name='logout'),
    path('register/',registerView, name='resister'),
]