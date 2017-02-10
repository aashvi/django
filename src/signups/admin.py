from django.contrib import admin

# Register your models here.
from .models import SignUp, Customer


class SignUpAdmin(admin.ModelAdmin):
	class Meta:
		model = SignUp


class CustomerAdmin(admin.ModelAdmin):
	class Meta:
		model = Customer


admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Customer)
