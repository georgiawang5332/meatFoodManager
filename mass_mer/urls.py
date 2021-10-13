from django.urls import path
from . import views

# Create your urls here.
app_name = 'mass_mer'
urlpatterns = [
  # Create
  # path('create/', views.stinstert, name='stinstert'),           # http://127.0.0.1:7878/posts/create
  # path('stdisplay/', views.stdisplay, name='stdisplay'),           # http://127.0.0.1:7878/posts/create
  # path('create/', views.stinstert, name='stinstert'),           # http://127.0.0.1:7878/posts/create
  # path('stdisplay/', views.stdisplay, name='stdisplay'),           # http://127.0.0.1:7878/posts/create

  path('create/', views.MassMerPersonCreate, name='stinstert'),           # http://127.0.0.1:7878/posts/create
  path('stdisplay/', views.MassMerPersonList, name='stdisplay'),
  path('edit/<int:id>/', views.MassMerPersonEdit, name='stedit'),
  path('update/<int:id>/', views.MassMerPersonUpdate, name='stupdate'),
  path('delete/<int:id>/', views.MassMerPersonDel, name='stdelete'),
  path('detail/<int:id>/', views.MassMerPersonDetail, name='stdetail'),  # http://127.0.0.1:7878/mass_mer/detail/3/

  # List
  path('MassMerList/', views.MassMerList, name='MassMerList'),                    # http://127.0.0.1:7878/mass_mer/list
  path('FoodVendorList/', views.FoodVendorList, name='FoodVendorList'),           # http://127.0.0.1:7878/mass_mer/list
  path('StorefrontList/', views.StorefrontList, name='StorefrontList'),           # http://127.0.0.1:7878/mass_mer/list
  path('RetailFactoryList/', views.RetailFactoryList, name='RetailFactoryList'),  # http://127.0.0.1:7878/mass_mer/list
  path('OtherList/', views.OtherList, name='OtherList'),                          # http://127.0.0.1:7878/mass_mer/list

  # Detail
  # path('<int:id>/massmerpersonDetail/', views.MassMerPersonDetail, name='massmerpersonDetail'),  # http://127.0.0.1:7878/posts/1/massmerpersonDetail

  # Update
  # path('<int:id>/update/', views.update, name='update'),  # http://127.0.0.1:7878/posts/1/update

  # Delete
  # path('<int:id>/delete/', views.delete, name='delete'),  # http://127.0.0.1:7878/posts/1/delete


  # CURD
  # path('create/', views.create, name='create'),           # http://127.0.0.1:7878/posts/create
  # path('<int:id>/detail/', views.detail, name='detail'),  # http://127.0.0.1:7878/posts/1/detail
  # path('list/', views.list, name='list'),                   # http://127.0.0.1:7878/posts/list
  # path('<int:id>/update/', views.update, name='update'),  # http://127.0.0.1:7878/posts/1/update
  # path('<int:id>/delete/', views.delete, name='delete'),  # http://127.0.0.1:7878/posts/1/delete
]
