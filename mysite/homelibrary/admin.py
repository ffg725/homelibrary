from django.contrib import admin

from .models import LibraryObject, Archive_Details, Author_Artist

# Register your models here.

admin.site.register(LibraryObject)
admin.site.register(Archive_Details)
admin.site.register(Author_Artist)