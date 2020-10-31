from django.urls import path
from . import views
from django.contrib.auth import logout

urlpatterns = [
    path(r'', views.signup, name= 'signup'),
    path(r'login/', views.loginpage, name= 'login'),
    path(r'logout/', views.logoutuser, name= 'logout'),
    
]
