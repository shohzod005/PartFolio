# Generated by Django 4.0.1 on 2023-03-21 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_me_remove_product_category_delete_category_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Me',
        ),
        migrations.AddField(
            model_name='gallery',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
