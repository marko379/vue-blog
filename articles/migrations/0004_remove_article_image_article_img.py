# Generated by Django 4.1 on 2022-10-30 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
