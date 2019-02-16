from django import forms

class CouponApplyForm(forms.Form):
	# TODO: Define form fields here
	code = forms.CharField()