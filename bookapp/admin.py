from django.contrib import admin

# Register your models here.
from .models import Book,Author

admin.site.register(Book)
# this use to show the stored details in uadmin pannel

admin.site.register(Author)