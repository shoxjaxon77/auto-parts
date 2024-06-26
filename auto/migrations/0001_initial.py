# Generated by Django 5.0.4 on 2024-05-31 19:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('image', models.ImageField(default='templates/BRAND.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Kategoriyalar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default_spare_parts.jpg', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Transportlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('modeli', models.CharField(max_length=100)),
                ('pozitsiya', models.CharField(max_length=50)),
                ('turi', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default_car.jpg', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ExtiyotQismlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('narxi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('malumot', models.TextField(blank=True)),
                ('miqdori', models.IntegerField(blank=True, null=True)),
                ('keltirilgan_sana', models.DateField()),
                ('picture', models.ImageField(default='default_image.jpg', upload_to='')),
                ('kategoriya_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto.kategoriyalar')),
                ('avto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto.transportlar')),
            ],
        ),
        migrations.CreateModel(
            name='Xaridlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soni', models.IntegerField(blank=True, null=True)),
                ('sana', models.DateField()),
                ('jihoz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto.extiyotqismlar')),
            ],
        ),
    ]
