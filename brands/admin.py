from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import Brand

class BrandInline(admin.StackedInline):
    model = Brand
    can_delete = False
    verbose_name_plural = 'brand'

class UserAdmin(BaseUserAdmin):
    inlines = (BrandInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)