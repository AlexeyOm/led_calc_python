from django import forms
from .models import Vendor
from .models import Cabinet

class CabinetForm(forms.ModelForm):

    class Meta:
        model = Cabinet
        fields = '__all__'