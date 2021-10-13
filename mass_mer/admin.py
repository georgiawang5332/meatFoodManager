from django.contrib import admin
from mass_mer.models import *


# Register your models here.

# 量販店
class Mass_MerInline(admin.StackedInline):
  model = Mass_Mer
  extra = 1


class Mass_MerAdmin(admin.ModelAdmin):
  list_display = (
    'company_name', 'company_principal', 'company_phone', 'cell_phone', 'address', 'uniform_numbers',
    'area', 'regional_app_num', 'cooperate_businmen', 'mailbox', 'capital',
  )
  fields = (
    'company_name', 'company_principal', 'company_phone', 'cell_phone', 'address', 'uniform_numbers',
    'area', 'regional_app_num', 'cooperate_businmen', 'mailbox', 'capital',
  )

  list_filter = ('company_name',)
  search_fields = ('company_name',)
  ordering = ('-mailbox',)


admin.site.register(Mass_Mer, Mass_MerAdmin)


# 量販店負責人
class Mass_Mer_PersonAdmin(admin.ModelAdmin):
  inlines = (Mass_MerInline,)
  list_display = (
    'mass_mer_principal',
    'certificate_num_principal',
    'telephone', 'address',
  )
  fields = (
    'mass_mer_principal',
    'certificate_num_principal',
    'telephone', 'address',
  )
  list_filter = ('certificate_num_principal',)
  search_fields = ('certificate_num_principal',)


admin.site.register(Mass_Mer_Person, Mass_Mer_PersonAdmin)  # 菜單

# admin.site.register(Mass_Mer)
# admin.site.register(Mass_Mer_Person)

# 攤位
admin.site.register(Food_Vendor)
admin.site.register(Food_Vendor_Person)
# 店面
admin.site.register(Storefront)
admin.site.register(Storefront_Person)
# 工廠/零售業
admin.site.register(Retail_Factory)
admin.site.register(Retail_Factory_Person)
# 其他
admin.site.register(Other)
admin.site.register(Other_Person)
