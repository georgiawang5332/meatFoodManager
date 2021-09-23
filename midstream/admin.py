from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Midstream)  # 中游商
class MidstreamAdmin(admin.ModelAdmin):
  list_display = ('id', 'store_name', 'store_holder', 'store_phoneNumber', 'store_address', 'store_email', 'store_notes')


admin.site.register(Midstream_person)  # 中游商負責人
class Midstream_person(admin.ModelAdmin):
  list_display = ('id', 'store_name', 'store_holder', 'store_phoneNumber', 'store_address', 'store_email', 'store_notes')
