from django.contrib import admin

from users_uci.models import User


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "date_joined",)
    exclude = ('slug',)


admin.site.register(User, UserAdmin)
