from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.signup, name= 'signup'),
    path(r'login/', views.loginpage, name= 'login'),
    
]
