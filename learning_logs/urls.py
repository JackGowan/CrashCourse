"""This is the APP url file"""

from django.conf.urls import url
from django.urls import path
from . import views


app_name = "learning_logs"

urlpatterns = [
 # Home page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/(?P<topic_id>)/$', views.topic, name='topic'),
    path('new_topic/$', views.new_topic, name='new_topic'),
    path('new_entry/(?P<topic_id>)/$', views.new_entry, name='new_entry'),
    path('edit_entry/(?P<entry_id>)/$', views.edit_entry, name='edit_entry'),  
        ]



# Page for editing an entry
# url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
# name='edit_entry'),



#url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

#url(r'^new_topic/$', views.new_topic, name='new_topic'),

# Detail page for a single topic
#url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

#     urlpatterns = [
#     path('about/', AboutPageView.as_view(), name='about'), # new
#     path('', HomePageView.as_view(), name='home'),
# ]