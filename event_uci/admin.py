from django.contrib import admin

from event_uci.models import Evento, User, Programa


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "date_joined",)
    exclude = ('slug',)


class EventAdmin(admin.ModelAdmin):
    fields = ["nombre", "fecha_inicio", "fecha_fin", "descripcion", "hora_inicio", "contacto", "ubicacion"]
    exclude = ('slug',)


class ProgramaAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(User, UserAdmin)
admin.site.register(Evento, EventAdmin)
admin.site.register(Programa, ProgramaAdmin)
