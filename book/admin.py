from django.contrib import admin

# Register your models here.
from .models import Book,Genre,Author


admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
