
from django.conf.urls import url
from django.urls import path
#from django.contrib.auth.views import login
from django.contrib.auth.views import LoginView
from . import views


app_name = "users"
    
	
urlpatterns = [
# Login page
path('login/',  LoginView.as_view(template_name='users/login.html'),name='login'),
path('logout/',  views.logout_view,name='logout'),
path('register/',  views.register,name='register'),



# Registration page
#url(r'^register/$', views.register, name='register'),


]



 # path('login/', 
 #        LoginView.as_view(
 #            template_name='users/login.html'
 #        ), 
 #        name="login"
# url(r'^login/$', login, {'template_name': 'users/login.html'},
# name='login'),



 # path('topics/(?P<topic_id>)/$', views.topic, name='topic'),
 # path('new_topic/$', views.new_topic, name='new_topic'),
 # path('new_entry/(?P<topic_id>)/$', views.new_entry, name='new_entry'),