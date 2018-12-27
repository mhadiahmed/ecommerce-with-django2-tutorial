from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
	
	name = models.CharField(max_length=200,db_index=True)
	slug = models.SlugField(max_length=200,db_index=True,unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = "Category"
		verbose_name_plural = "Categorys"

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_list_category',args=[self.slug])

class Product(models.Model):

	category 	= models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
	name 		= models.CharField(max_length=200,db_index=True)
	slug 		= models.SlugField(max_length=200,db_index=True)
	Image 		= models.ImageField(blank=True)
	description = models.TextField(blank=True)
	price 		= models.DecimalField(max_digits=10,decimal_places=2)
	stock 		= models.PositiveIntegerField()
	available 	= models.BooleanField(default=True)
	created 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created',)
		index_together = (('id','slug'),)
		verbose_name = "Product"
		verbose_name_plural = "Products"

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_detail',args=[self.id,self.slug])