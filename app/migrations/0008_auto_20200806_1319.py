# Generated by Django 3.0.6 on 2020-08-06 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200806_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, default='images/brak_zdjecia.png', null=True, upload_to='image'),
        ),
    ]