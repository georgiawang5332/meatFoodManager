from django.contrib import admin
from .models import *


#
# # Register your models here.
# admin.site.register(UserProfile)  # 店家(餐廳)

class UserProfileAdmin(admin.ModelAdmin):
  list_display = ('user', 'user_info', 'phone', 'email', 'city', 'website')

  def user_info(self, obj):
    return obj.description

  def get_queryset(self, request):
    queryset = super(UserProfileAdmin, self).get_queryset(request)
    queryset = queryset.order_by('-phone')
    return queryset

  user_info.short_description = "Info 2"
  # list_display = ('user', 'image', 'phone', 'email', 'city', 'website', 'description')


#   list_filter = ('phone',)
#   search_fields = ('phone',)
#   fields = ('user', 'image', 'phone', 'email', 'city', 'website',
#             'description')  # 這將會使得price欄位出現在restaurant欄位之前，而且name、is_spicy和comment欄位都不會出現，不能被編輯。
#   ordering = ('-city',)
#   list_display_link = ('image', 'phone', 'city', 'website', 'description')
#
#   def user_info(self, obj):
#     return obj.description
#
#   def get_queryset(self, request):
#     queryset = super(UserProfileAdmin, self).get_queryset(request)
#     queryset = queryset.order_by('-phone')
#     return queryset
#
#   class Meta:
#     modle = UserProfile
#
#
admin.site.register(UserProfile, UserProfileAdmin)
