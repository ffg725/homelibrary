# Generated by Django 4.1.5 on 2023-01-14 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homelibrary', '0003_alter_archive_details_meta_data_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive_details',
            name='resource_url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='author_artist',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
    ]