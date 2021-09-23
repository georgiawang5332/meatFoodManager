from django.urls import path
from . import views

# Create your urls here.
app_name = 'midstream'
urlpatterns = [
  # CURD
  path('create/', views.create, name='create'),           # http://127.0.0.1:7878/posts/create
  path('<int:id>/detail/', views.detail, name='detail'),  # http://127.0.0.1:7878/posts/1/detail
  # path('detail/', views.detail, name='detail'),  # http://127.0.0.1:7878/posts/1/detail
  path('list/', views.list, name='list'),                 # http://127.0.0.1:7878/posts/list
  path('<int:id>/update/', views.update, name='update'),  # http://127.0.0.1:7878/posts/1/update
  # path('update/', views.update, name='update'),  # http://127.0.0.1:7878/posts/1/update
  path('<int:id>/delete/', views.delete, name='delete'),  # http://127.0.0.1:7878/posts/1/delete
  # path('delete/', views.delete, name='delete'),  # http://127.0.0.1:7878/posts/1/delete
]
