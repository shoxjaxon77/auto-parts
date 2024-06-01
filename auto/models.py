from django.db import models

class Kategoriyalar(models.Model):
    nomi = models.CharField(max_length=100)
    image = models.ImageField(default='default_spare_parts.jpg')
    
    def __str__(self):
        return self.nomi

class Transportlar(models.Model):
    nomi = models.CharField(max_length=100)
    modeli = models.CharField(max_length=100)
    pozitsiya = models.CharField(max_length=50)
    turi = models.CharField(max_length=100)
    image = models.ImageField(default='default_car.jpg')
    def __str__(self):
        return self.nomi

class ExtiyotQismlar(models.Model):
    nomi = models.CharField(max_length=100)
    narxi = models.DecimalField(max_digits=10,decimal_places=2)
    malumot = models.TextField(blank=True)
    miqdori = models.IntegerField(blank=True,null=True)
    keltirilgan_sana = models.DateField()
    kategoriya_id = models.ForeignKey(Kategoriyalar,on_delete=models.CASCADE)
    picture = models.ImageField(default='default_image.jpg')
    avto = models.ForeignKey(Transportlar,on_delete=models.CASCADE)
    def __str__(self):
        return self.nomi
    



    
class Brands(models.Model):
    nomi = models.CharField(max_length=100)
    image = models.ImageField(default='templates/BRAND.png')

    def __str__(self):
        return self.nomi

class Xaridlar(models.Model):
    jihoz_id = models.ForeignKey(ExtiyotQismlar,on_delete=models.CASCADE)
    soni = models.IntegerField(blank=True,null=True)
    sana = models.DateField()
