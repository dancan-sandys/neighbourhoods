from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import logout

urlpatterns = [
    url(r'^$', views.signup, name= 'signup'),
    url(r'^login/$', views.loginpage, name= 'login'),
    url(r'logout/$', views.logoutuser, name= 'logout'),
    url(r'home/$', views.home, name= 'home'),
    url(r'myneighbourhood/$', views.myneigbourhood, name= 'myneighbourhood'),
    url(r'profile/$', views.profile, name = 'profile'),
    url(r'neigbourhoods/$', views.allneighbourhoods, name = 'allneighbourhoods'),
    url(r'businessses/$', views.businesses, name = 'businesses'),
    url(r'accounts/create/$', views.createaccount, name='createaccount'),
    url(r'business/create/$',views.createbusiness, name='createbusiness'),
    url(r'business/single/(\d+)$', views.singlebusiness, name='single_business')
    
]
