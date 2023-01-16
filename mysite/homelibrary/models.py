from django.db import models

# Create your models here.

class Author_Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.CharField(max_length=500)

class Archive_Details(models.Model):
    size = models.CharField(max_length=50)
    meta_data_type = models.CharField(max_length=20)
    resource_url = models.CharField(max_length=255)

class LibraryObject(models.Model):
    archive_details = models.ManyToManyField(Archive_Details)
    author_artist = models.ManyToManyField(Author_Artist)
    description_text = models.TextField(max_length=500)
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    physical_attribute = models.CharField(max_length=50)



