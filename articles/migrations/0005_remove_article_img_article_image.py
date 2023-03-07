# Generated by Django 4.1 on 2022-10-30 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_article_image_article_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='img',
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
