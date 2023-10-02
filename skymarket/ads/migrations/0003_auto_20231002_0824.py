# Generated by Django 3.2.6 on 2023-10-02 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
