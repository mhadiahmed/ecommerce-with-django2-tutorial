from django.contrib import admin
from .models import Category,Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	'''
		Admin View for Category
	'''
	list_display = ('name','slug',)
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
	'''
		Admin View for Product
	'''
	list_display = ('name','slug','category','price','stock','available','created','updated',)
	list_filter = ('available','created','updated','category',)
	list_editable = ('price','stock','available',)
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Product, ProductAdmin)