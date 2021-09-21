from django.contrib import admin
from .models import Products,Catagories
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class ProductsModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('description')
admin.site.register(Products,ProductsModelAdmin)
admin.site.register(Catagories)