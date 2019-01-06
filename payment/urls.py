from django.urls import re_path
from . import views


app_name = 'payment'

urlpatterns = [
	re_path(r'^process/$',views.payment_process,name='process'),
	re_path(r'^done/$',views.payment_done,name='done'),
	re_path(r'^canceled/$',views.payment_canceled,name='canceled'),
]