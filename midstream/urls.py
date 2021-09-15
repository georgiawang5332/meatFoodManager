from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from midstream.views import *

# Create your urls here.
app_name = 'midstream'
urlpatterns = [
  path('list/', views.list, name='list'),  # http://127.0.0.1:8000/posts/list
]
