from django.contrib import admin

from programs_uci.models import Programa


# Register your models here.

class ProgramaAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(Programa, ProgramaAdmin)
