# Generated by Django 4.1 on 2023-04-25 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0009_delete_anonymous_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_photo',
            name='avatar_photo',
            field=models.ImageField(blank=True, default='avatar.png', null=True, upload_to='avatar_images/'),
        ),
        migrations.AlterField(
            model_name='user_photo',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_photo',
            name='user_img',
            field=models.ImageField(blank=True, default='avatar.png', null=True, upload_to='user_profile_images/'),
        ),
    ]
