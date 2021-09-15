# from django.db import models
# from django.contrib.auth.models import User
#
#
# # Create your models here.
# class UserProfile(models.Model):
#   user = models.OneToOneField(User, on_delete=models.CASCADE, default='', primary_key=True, )
#   city = models.CharField(max_length=100, default='')
#   email = models.EmailField(
#     verbose_name='email address',
#     max_length=255,
#     unique=True,
#   )
#   phone = models.IntegerField(default=0)
#   website = models.URLField(default='')
#   image = models.ImageField(upload_to='profile_image', blank=True)
#   description = models.CharField(max_length=100, default='')
#
#
#   def __str__(self):
#     return self.user.username
