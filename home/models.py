from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

# How to Write Your First Custom Model Manager (Django Tutorial) | Part 40
class UserProfileManager(models.Manager):
  def get_queryset(self):
    return super(UserProfileManager, self).get_queryset().filter(city='london')

class UserProfile(models.Model):
  objects = None
  user = models.OneToOneField(User, on_delete=models.CASCADE, default='', primary_key=True, )
  description = models.TextField(max_length=100, default='')
  city = models.CharField(max_length=100, default='')
  email = models.EmailField(_('郵件信箱'), max_length=254, default='')
  website = models.URLField(default='')
  phone = models.CharField(max_length=10, default=0)
  image = models.ImageField(upload_to='profile_image', blank=True)

  london = UserProfileManager()

  def __str__(self):
    return self.user.username


@receiver(post_save, sender=User)
def create_profile(instance, created, **kwargs):
  if created:
    UserProfile.objects.create(user=instance)
  instance.userprofile.save()


post_save.connect(create_profile, sender=User)
