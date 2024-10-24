"""
URL configuration for eventos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from event_uci.views import EventoList, getEventDetail
from eventos import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("users/", include("users_uci.urls")),
                  path("programs/", include("programs_uci.urls")),

                  path('api/events', EventoList.as_view(), name="myapp"),
                  path('api/event/register', EventoList.as_view(), name='register_event'),
                  path('api/event/<slug:slug_name>', getEventDetail, name='detail_event'),
                  path('api/event/update/<slug:slug_name>', EventoList.as_view(), name='update_event'),
                  path('api/event/delete/<slug:slug_name>', EventoList.as_view(), name='delete_event'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
