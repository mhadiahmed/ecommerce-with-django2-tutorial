from django.contrib import admin
from .models import OrderItem,order
from import_export.admin import ImportExportActionModelAdmin
from django.urls import reverse
from django.utils.safestring import mark_safe


def order_pdf(obj):
	return mark_safe('<a href="{}">PDF</a>'.format(reverse('orders:admin_order_pdf',args=[obj.id])))

order_pdf.short_description = 'Order PDF'



class OrderItemAdmin(admin.TabularInline):
	'''
		Admin View for OrderItem
	'''
	model = OrderItem
	raw_id_fields = ['product']


class OrderAdmin(ImportExportActionModelAdmin):
	'''
		Admin View for Order
	'''
	list_display = ('id','first_name','last_name','address','email','city','postal_code','paid',order_pdf,)
	list_filter = ('paid','created','updated',)
	search_fields = ['first_name','last_name','email']
	inlines = [
	OrderItemAdmin,
	]

admin.site.register(order, OrderAdmin)