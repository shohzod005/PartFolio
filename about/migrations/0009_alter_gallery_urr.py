# Generated by Django 4.0.1 on 2023-03-21 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_rename_url_gallery_urr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='urr',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
