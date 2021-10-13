from django import forms
from mass_mer.models import *

class stform(forms.ModelForm):
  class Meta:
    model = Mass_Mer_Person
    fields = '__all__'
    # fields = ['mass_mer_principal', 'certificate_num_principal', 'telephone', 'address']
