from django.contrib import admin
from midstream.models import *


# Register your models here.
# admin.site.register(Midstream)  # 中游商

class MidstreamInline(admin.StackedInline):
  model = Midstream
  extra = 1


class MidstreamAdmin(admin.ModelAdmin):
  list_display = (
    'id', 'company_Name', 'company_principal', 'uniform_numbers', 'registration_status', 'register_phone',
    'registered_address', 'company_email', 'company_website', 'company_photos', 'registration_type',
    'registration_authority', 'company_notes', 'create_date', 'last_modified')
  fields = (
    'company_Name', 'company_principal', 'uniform_numbers', 'registration_status', 'register_phone',
    'registered_address', 'company_email', 'company_website', 'company_photos', 'registration_type',
    'registration_authority', 'company_notes')

  list_filter = ('company_Name',)
  search_fields = ('company_Name',)
  ordering = ('-company_email',)


admin.site.register(Midstream, MidstreamAdmin)  # 菜單


# admin.site.register(Midstream_person)  # 中游商負責人

class MidstreamPersonAdmin(admin.ModelAdmin):
  inlines = (MidstreamInline,)
  list_display = (
    'id', 'company_representative', 'person_ID', 'local_phone', 'cell_phone', 'person_email', 'create_date_p',
    'last_modified_p')
  fields = (
    'company_representative', 'person_ID', 'local_phone', 'cell_phone', 'person_email')

  list_filter = ('person_email',)
  search_fields = ('person_email',)
  # ordering = ('-person_ID')


admin.site.register(Midstream_person, MidstreamPersonAdmin)  # 菜單
