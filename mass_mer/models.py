from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.
# results = Mass_Mer_Person.objects.all()
# results = Mass_Mer_Person.objects.create(user=user, title="some time")
class Mass_Mer_PersonManager(models.Manager):
  def active(self, *arg, **kwargs):
    return super(Mass_Mer_PersonManager, self).filter(mass_mer_principal=False)

# Mass_Mer_Person.objects.all() = super(Mass_Mer_PersonManager, self).all()
# def get_queryset(self):
#   return super(Mass_Mer_PersonManager, self).get_queryset(mass_mer_principal=False).filter(city='London')

# 量販店
class Mass_Mer(models.Model):
  company_name       = models.CharField(_('公司名稱'), max_length=255)
  company_principal  = models.ForeignKey('Mass_Mer_Person', on_delete=models.CASCADE, related_name='midstream',
                              null=True, blank=True, default='',
                              help_text=_('公司負責人'))  # 店家名字 related_name 查詢之類的
  company_phone      = models.CharField(_('公司電話'), max_length=10, blank=True,
                              help_text=_('手機，ex：0225445666，***直接輸入數字，不用此符號「-」'))
  cell_phone         = models.CharField(_('手機電話'), max_length=10, blank=True,
                              help_text=_('手機，ex：0912345678，***直接輸入數字，不用此符號「-」'))
  address            = models.CharField(_('登記地址'), max_length=255)
  uniform_numbers    = models.CharField(_('統一編號'), max_length=8, blank=True,
                              help_text=_('企業請提供統一編號 (8碼，ex: 12345678)；個人請提供身分證字號'))
  area               = models.CharField(_('區域'), max_length=5, blank=True,
                              help_text=_('ex: 文山區'))
  regional_app_num   = models.CharField(_('地區申請編號'), max_length=10, blank=True,
                              help_text=_('ex: 1234567890'))
  cooperate_businmen = models.CharField(_('合作的中游商'), max_length=255, blank=True,
                              help_text=_(''))
  mailbox            = models.CharField(_('信箱'), max_length=8, blank=True,
                              help_text=_('企業請提供統一編號 (8碼，ex: 12345678)；個人請提供身分證字號'))
  capital            = models.CharField(_('資本額'), max_length=255, blank=True,
                              help_text=_('ex: 200,000,000'))
  approved_date      = models.DateTimeField(_('核准設立日期'), auto_now_add=True, help_text=_(''))


class Mass_Mer_Person(models.Model):  # 量販店負責人
  mass_mer_principal        = models.CharField(_('量販店負責人'), max_length=255, blank=True,
                               help_text=_(''))
  certificate_num_principal = models.CharField(_('負責人證號'), max_length=10, blank=True,
                               help_text=_('格式為身分證字號（1 碼，限大寫英文字）+ 身分字號（最長 9 碼，限數字'))
  telephone                 = models.CharField(_('手機電話'), max_length=10, blank=True,
                               help_text=_('手機，ex：0912345678，***直接輸入數字，不用此符號「-」'))
  address                   = models.CharField(_('地址'), max_length=255, blank=True,
                               help_text=_(''))

  objects = Mass_Mer_PersonManager()

  def get_absolute_url(self):
    return reverse('mass_mer:stdetail', kwargs={'id': self.id})

  def __str__(self):
    return self.mass_mer_principal

  def __unicode__(self):
    return self.mass_mer_principal

# 生食攤商
class Food_Vendor(models.Model):
  company_name              = models.CharField(_('攤位名稱'), max_length=255)
  company_principal         = models.ForeignKey('Food_Vendor_Person', on_delete=models.CASCADE, related_name='midstream',
                                       null=True, blank=True, default='',
                                       help_text=_('公司負責人'))  # 店家名字 related_name 查詢之類的
  company_phone             = models.CharField(_('公司電話'), max_length=10, blank=True,
                                       help_text=_('手機，ex：0225445666，***直接輸入數字，不用此符號「-」'))
  cell_phone                = models.CharField(_('手機電話'), max_length=10, blank=True,
                                       help_text=_('手機，ex：0912345678，***直接輸入數字，不用此符號「-」'))
  address                   = models.CharField(_('登記地址'), max_length=255)
  uniform_numbers           = models.CharField(_('統一編號'), max_length=8, blank=True,
                                       help_text=_('企業請提供統一編號 (8碼，ex: 12345678)；個人請提供身分證字號'))
  area                      = models.CharField(_('區域'), max_length=5, blank=True,
                                       help_text=_('ex: 台北市'))
  vendors_stand_num         = models.CharField(_('攤位編號'), max_length=5, blank=True,
                                       help_text=_('需10碼，ex: 1234567890'))
  regional_app_num          = models.CharField(_('地區申請編號'), max_length=10, blank=True,
                                                 help_text=_('ex: 1234567890'))
  cooperate_businmen        = models.CharField(_('合作的中游商'), max_length=255, blank=True,
                                       help_text=_(''))
  mailbox                   = models.CharField(_('信箱'), max_length=8, blank=True,
                                       help_text=_('企業請提供統一編號 (8碼，ex: 12345678)；個人請提供身分證字號'))
  capital                   = models.CharField(_('資本額'), max_length=255, blank=True,
                                       help_text=_('ex: 200,000,000'))
  approved_date             = models.DateTimeField(_('核准設立日期'), auto_now_add=True, help_text=_(''))


class Food_Vendor_Person(models.Model):
  vendors_stand_principal       = models.CharField(_('攤位負責人'), max_length=255, blank=True,
                                       help_text=_(''))
  vendors_stand_certificate_num = models.CharField(_('負責人證號'), max_length=10, blank=True,
                                       help_text=_('格式為身分證字號（1 碼，限大寫英文字）+ 身分字號（最長 9 碼，限數字'))
  telephone                     = models.CharField(_('電話'), max_length=10, blank=True,
                                       help_text=_('手機，ex：0912345678，***直接輸入數字，不用此符號「-」'))
  address                       = models.CharField(_('地址'), max_length=255, blank=True,
                                       help_text=_(''))


# 店面
class Storefront(models.Model):
  company_name               = models.CharField(_('公司(攤位)名稱'), max_length=255)
  company_principal          = models.ForeignKey('Storefront_Person', on_delete=models.CASCADE, related_name='midstream',
                                        null=True, blank=True, default='',
                                        help_text=_('公司負責人'))  # 店家名字 related_name 查詢之類的
  company_phone              = models.CharField(_('公司電話'), max_length=10, blank=True,
                                        help_text=_('手機，ex：0225445666，***直接輸入數字，不用此符號「-」'))
  cell_phone                 = models.CharField(_('手機電話'), max_length=10, blank=True,
                                        help_text=_('手機，ex：0912345678，***直接輸入數字，不用此符號「-」'))
  address                    = models.CharField(_('登記地址'), max_length=255)
  uniform_numbers            = models.CharField(_('統一編號'), max_length=8, blank=True,
                                        help_text=_('企業請提供統一編號 (8碼，ex: 12345678)；個人請提供身分證字號'))
  area                       = models.CharField(_('區域'), max_length=5, blank=True,
                                        help_text=_('ex: 文山區'))
  regional_app_num           = models.CharField(_('地區申請編號'), max_length=10, blank=True,
                                        help_text=_('ex: 1234567890'))
  cooperate_businmen         = models.CharField(_('合作的中游商'), max_length=255, blank=True,
                                        help_text=_(''))
  mailbox                    = models.CharField(_('信箱'), max_length=8, blank=True,
                                        help_text=_('企業請提供統一編號 (8碼，ex: 12345678)；個人請提供身分證字號'))
  capital                    = models.CharField(_('資本額'), max_length=255, blank=True,
                                        help_text=_('ex: 200,000,000'))
  approved_date              = models.DateTimeField(_('核准設立日期'), auto_now_add=True, help_text=_(''))


class Storefront_Person(models.Model):
  storefront_principal       = models.CharField(_('店面負責人'), max_length=255, blank=True,
                                        help_text=_(''))
  storefront_certificate_num = models.CharField(_('負責人證號'), max_length=10, blank=True,
                                        help_text=_('格式為身分證字號（1 碼，限大寫英文字）+ 身分字號（最長 9 碼，限數字'))
  telephone                  = models.CharField(_('電話'), max_length=10, blank=True,
                                        help_text=_('手機，ex：0912345678，***直接輸入數字，不用此符號「-」'))
  address                    = models.CharField(_('地址'), max_length=255, blank=True,
                                        help_text=_(''))


# 零售(工廠)
class Retail_Factory(models.Model):
  company_name               = models.CharField(_('公司名稱'), max_length=255)
  company_principal          = models.ForeignKey('Retail_Factory_Person', on_delete=models.CASCADE, related_name='midstream',
                                     null=True, blank=True, default='',
                                     help_text=_('公司負責人'))  # 店家名字 related_name 查詢之類的
  company_phone              = models.CharField(_('公司電話'), max_length=10, blank=True,
                                     help_text=_('手機，ex：0225445666，***直接輸入數字，不用此符號「-」'))
  cell_phone                 = models.CharField(_('手機電話'), max_length=10, blank=True,
                                     help_text=_('手機，ex：0912345678，***直接輸入數字，不用此符號「-」'))
  address                    = models.CharField(_('登記地址'), max_length=255)
  uniform_numbers            = models.CharField(_('統一編號'), max_length=8, blank=True,
                                     help_text=_('企業請提供統一編號 (8碼，ex: 12345678)；個人請提供身分證字號'))
  area                       = models.CharField(_('區域'), max_length=5, blank=True,
                                     help_text=_('ex: 文山區'))
  regional_app_num           = models.CharField(_('地區申請編號'), max_length=10, blank=True,
                                     help_text=_('ex: 1234567890'))
  cooperate_businmen         = models.CharField(_('合作的中游商'), max_length=255, blank=True,
                                     help_text=_(''))
  mailbox                    = models.CharField(_('信箱'), max_length=8, blank=True,
                                     help_text=_('企業請提供統一編號 (8碼，ex: 12345678)；個人請提供身分證字號'))
  capital                    = models.CharField(_('資本額'), max_length=255, blank=True,
                                     help_text=_('ex: 200,000,000'))
  approved_date              = models.DateTimeField(_('核准設立日期'), auto_now_add=True, help_text=_(''))


class Retail_Factory_Person(models.Model):
  retail_factory_principal       = models.CharField(_('工廠負責人'), max_length=255, blank=True,
                                      help_text=_(''))
  retail_factory_certificate_num = models.CharField(_('負責人證號'), max_length=10, blank=True,
                                      help_text=_('格式為身分證字號（1 碼，限大寫英文字）+ 身分字號（最長 9 碼，限數字'))
  telephone                      = models.CharField(_('手機號碼'), max_length=10, blank=True,
                                      help_text=_('手機，ex：0912345678，***直接輸入數字，不用此符號「-」'))
  address                        = models.CharField(_('地址'), max_length=255, blank=True,
                                      help_text=_(''))


# 其他
class Other(models.Model):
  company_name       = models.CharField(_('公司名稱'), max_length=255)
  company_principal  = models.ForeignKey('Other_Person', on_delete=models.CASCADE, related_name='midstream',
                                    null=True, blank=True, default='',
                                    help_text=_('公司負責人'))
  company_phone      = models.CharField(_('公司電話'), max_length=10, blank=True,
                                    help_text=_('手機，ex：0225445666，***直接輸入數字，不用此符號「-」'))
  cell_phone         = models.CharField(_('手機電話'), max_length=10, blank=True,
                                    help_text=_('手機，ex：0912345678，***直接輸入數字，不用此符號「-」'))
  address            = models.CharField(_('登記地址'), max_length=255)
  uniform_numbers    = models.CharField(_('統一編號'), max_length=8, blank=True,
                                    help_text=_('企業請提供統一編號 (8碼，ex: 12345678)；個人請提供身分證字號'))
  area               = models.CharField(_('區域'), max_length=5, blank=True,
                                    help_text=_('ex: 文山區'))
  regional_app_num   = models.CharField(_('地區申請編號'), max_length=10, blank=True,
                                    help_text=_('ex: 1234567890'))
  cooperate_businmen = models.CharField(_('合作的中游商'), max_length=255, blank=True,
                                    help_text=_(''))
  mailbox            = models.CharField(_('信箱'), max_length=8, blank=True,
                                    help_text=_('企業請提供統一編號 (8碼，ex: 12345678)；個人請提供身分證字號'))
  capital            = models.CharField(_('資本額'), max_length=255, blank=True,
                                    help_text=_('ex: 200,000,000'))
  approved_date      = models.DateTimeField(_('核准設立日期'), auto_now_add=True, help_text=_(''))


class Other_Person(models.Model):
  other_principal       = models.CharField(_('其他負責人'), max_length=255, blank=True,
                                    help_text=_(''))
  other_certificate_num = models.CharField(_('負責人證號'), max_length=10, blank=True,
                                    help_text=_('格式為身分證字號（1 碼，限大寫英文字）+ 身分字號（最長 9 碼，限數字'))
  telephone             = models.CharField(_('電話'), max_length=10, blank=True,
                                    help_text=_('手機，ex：0912345678，***直接輸入數字，不用此符號「-」'))
  address               = models.CharField(_('地址'), max_length=255, blank=True,
                                    help_text=_(''))
