# Generated by Django 3.2.6 on 2023-10-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='django_media/avatars', verbose_name='Аватар'),
        ),
    ]
