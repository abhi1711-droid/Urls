from django.contrib import admin

# Register your models here.
from users.models import CustomUserModel, Url


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone']


admin.site.register(CustomUserModel, UserAdmin)


class UrlAdmin(admin.ModelAdmin):
    list_display = ['id', 'original_link', 'short_link', 'created_at', 'clicks']


admin.site.register(Url, UrlAdmin)
