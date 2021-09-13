from django.contrib import admin
from .models import Category, Product
# Register your models here.


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category)
admin.site.register(Product)
