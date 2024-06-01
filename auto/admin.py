from django.contrib import admin
from .models import Kategoriyalar,ExtiyotQismlar,Brands,Transportlar,Xaridlar

class BrandAdmin(admin.ModelAdmin):
    list_display = ['nomi','image']

class ExtiyotQismlarAdmin(admin.ModelAdmin):
    list_display=['nomi','narxi','malumot','miqdori','keltirilgan_sana']

class KategoriyalarAdmin(admin.ModelAdmin):
    list_display = ['nomi','image']

class TransportAdmin(admin.ModelAdmin):
    list_display = ['nomi','modeli','pozitsiya','turi']

class XaridAdmin(admin.ModelAdmin):
    list_display = ['jihoz_id','soni','sana']

admin.site.register(Kategoriyalar,KategoriyalarAdmin)
admin.site.register(ExtiyotQismlar,ExtiyotQismlarAdmin)
admin.site.register(Brands,BrandAdmin)
admin.site.register(Transportlar,TransportAdmin)
admin.site.register(Xaridlar,XaridAdmin)



