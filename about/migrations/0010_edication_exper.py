# Generated by Django 4.0.1 on 2023-03-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_alter_gallery_urr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Exper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
            ],
        ),
    ]