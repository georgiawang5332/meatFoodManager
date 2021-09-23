from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import *

# Create your urls here.
app_name = 'home'

urlpatterns = [
  path('profile/', views.profile, name='profile'),
  path('contact/', views.contact, name='contact'),
  path('', views.home, name='home'),
  # path('', views.HomeView, name='home'),

  #   login / logout / register
  path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
  path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/login.html'), name='logout'),

  path('accounts/register/', views.register, name='register'),

  # 密碼改變
  path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
  # 密碼改變成功
  path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

  # 忘記密碼 重設密碼
  path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
  # 忘記密碼 重設密碼 成功
  path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
  #
  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
  # 密碼已更改
  path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
