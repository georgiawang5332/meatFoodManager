from django import forms
from midstream.models import *

# Create your models here.
class MidstreamForm(forms.ModelForm):
  class Meta:
    model = Midstream
    fields = '__all__'

