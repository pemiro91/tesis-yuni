from django.contrib import admin

from event_uci.models import Evento


# Register your models here.


class EventAdmin(admin.ModelAdmin):
    fields = ["nombre", "fecha_inicio", "fecha_fin", "descripcion", "hora_inicio", "contacto", "ubicacion"]
    exclude = ('slug',)


admin.site.register(Evento, EventAdmin)
