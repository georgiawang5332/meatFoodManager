from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
# 1. 公司
class Midstream(models.Model):  # 中游商
  # Registration_Status_CHOICES = (
  #   ('STOP', '停業'),
  #   ('Approved', '核准設立'),
  #   ('Not_Applied', '未申請'),
  # )
  company_Name = models.CharField(_('公司名稱'), max_length=255)  # 公司名稱
  company_principal = models.ForeignKey('Midstream_person', on_delete=models.CASCADE, related_name='midstream',
                                        null=True, blank=True, default='',
                                        help_text=_('公司負責人'))  # 店家名字 related_name 查詢之類的
  uniform_numbers = models.CharField(_('統一編號'), max_length=8, blank=True,
                                     help_text=_('企業請提供統一編號 (8碼，ex: 12345678)；個人請提供身分證字號'))  # 統一編號
  registration_status = models.CharField(
    _('註冊狀態'),
    max_length=100,
    # choices=Registration_Status_CHOICES,
    # default='STOP',
    null=True,
    blank=True,
    help_text=_(
      '自行填寫格式為 :  "停業"&nbsp;&nbsp;&nbsp;"未申請"&nbsp;&nbsp;&nbsp;"核准設立 - 合夥/各人 (核准文號: 1090821289)"&nbsp;&nbsp;&nbsp;"其他原因"。 '),
  )  # 登記狀態
  register_phone = models.CharField(_('登記電話'), max_length=10, blank=True,
                                    help_text=_('手機，ex：0912-345-678，***直接輸入數字，不用此符號「-」'))  # 登記電話
  registered_address = models.CharField(_('登記地址'), max_length=255)  # 登記地址
  company_email = models.EmailField(
    _('郵件信箱'),
    max_length=255,
    blank=True,
    default="",
    help_text='★★★必需的。 添加有效的電子郵件地址',
  )  # 公司信箱
  company_website = models.URLField(_('公司網站'), max_length=255)  # 公司網站
  company_photos = models.ImageField(_('公司照片'), upload_to='companies', blank=True)  # 公司照片
  registration_type = models.CharField(_('登記種類'), max_length=255, help_text=_('ex: 商業登記'))  # 登記種類
  registration_authority = models.CharField(_('登記機關'), max_length=255, help_text=_('ex: XX(縣市)政府'))  # 登記機關
  company_notes = models.TextField(_('公司筆記'), blank=True)  # 公司筆記
  create_date = models.DateTimeField(_('儲存日期'), auto_now_add=True)
  last_modified = models.DateTimeField(_('最後修改日期'), auto_now=True)

  def __str__(self):
    return self.company_Name

  def __unicode__(self):
    return self.company_Name

  class Meta:
    ordering = ['-create_date', '-last_modified']


# 2. 負責人principal
class Midstream_person(models.Model):
  company_representative = models.CharField(_('公司負責人'), max_length=100)  # 公司負責人
  person_ID = models.CharField(
    _('負責人證號'), max_length=10,
    help_text=_('格式為身分證字號（1 碼，限大寫英文字）+ 身分字號（最長 9 碼，限數字)'), )  # 負責人ID
  local_phone = models.CharField(_('負責人市內電話'), max_length=10,
                                 help_text=_('市話，ex：02-1234-5678，***直接輸入數字，不用此符號「-」'))  # 負責人室電
  cell_phone = models.CharField(_('負責人手機'), max_length=10,
                                help_text=_('手機，ex: 0912-123-456，***直接輸入數字，不用此符號「-」'))  # 負責人手機
  person_email = models.EmailField(
    _('負責人信箱'),
    max_length=255,
    blank=True,
    default="",
    help_text='★★★必需的。 添加有效的電子郵件地址',
  )  # 負責人信箱
  create_date_p = models.DateTimeField(_('儲存日期'), auto_now_add=True)
  last_modified_p = models.DateTimeField(_('最後修改日期'), auto_now=True)

  def __str__(self):
    return self.company_representative

  def __unicode__(self):
    return self.company_representative
