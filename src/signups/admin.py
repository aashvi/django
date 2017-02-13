from django.contrib import admin

# Register your models here.
from .models import SignUp, Customer, Person, Article, Location, Photo, Video, Like


class SignUpAdmin(admin.ModelAdmin):
	class Meta:
		model = SignUp


class CustomerAdmin(admin.ModelAdmin):
	class Meta:
		model = Customer



admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Customer)
admin.site.register(Person)
admin.site.register(Article)
admin.site.register(Location)
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Like)