# Generated by Django 4.1.5 on 2023-01-14 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author_Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('biography', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_text', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('physical_attribute', models.CharField(max_length=50)),
                ('author_artist', models.ManyToManyField(to='homelibrary.author_artist')),
            ],
        ),
    ]
