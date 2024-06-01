from django import forms

from .models import ExtiyotQismlar,Transportlar,Xaridlar,Brands

class TransportlarForm(forms.ModelForm):
    class Meta:
        model = Transportlar
        fields = ('nomi','modeli','pozitsiya','turi','image')


class ExtiyotQismForm(forms.ModelForm):
    class Meta:
        model = ExtiyotQismlar
        fields = ('nomi','narxi','malumot','miqdori','keltirilgan_sana','kategoriya_id','picture','avto')  


class XaridlarForm(forms.ModelForm):
    class Meta:
        model = Xaridlar
        fields = ('jihoz_id','soni','sana')

class BrandsForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = ('nomi','image')

