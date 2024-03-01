from django.db import models
from django.contrib import admin
class BookData(models.Model):
	bookID=models.IntegerField(primary_key=True);
	bookname=models.CharField(max_length=50);
	authorname=models.CharField(max_length=50);
	dopublication=models.DateField();
	price=models.IntegerField();
class BookDataAdmin(admin.ModelAdmin):
	list_display=("bookID","bookname","authorname","dopublication","price");