from django.contrib import admin
from .models import BookData,BookDataAdmin
admin.site.register(BookData,BookDataAdmin)