# Generated by Django 4.1 on 2023-01-06 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_remove_article_comment2_article_comment2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='comment2',
        ),
        migrations.DeleteModel(
            name='Comments2',
        ),
    ]
