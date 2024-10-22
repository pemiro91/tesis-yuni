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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from event_uci.views import EventoList, UserApi, getProfile, getEventDetail, ProgramsList, getProgramDetail
from eventos import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view()),

    path('api/events', EventoList.as_view(), name="myapp"),
    path('api/event/register', EventoList.as_view(), name='register_event'),
    path('api/event/<slug:slug_name>', getEventDetail, name='detail_event'),
    path('api/event/update/<slug:slug_name>', EventoList.as_view(), name='update_event'),
    path('api/event/delete/<slug:slug_name>', EventoList.as_view(), name='delete_event'),

    path('api/users', UserApi.as_view(), name='users'),
    path('api/user/register', UserApi.as_view(), name='register'),
    path('api/user/profile', getProfile, name='profile'),
    path('api/user/profile/update/<slug:slug_username>', UserApi.as_view(), name='profile_update'),

    path('api/programs', ProgramsList.as_view()),
    path('api/program/register', ProgramsList.as_view(), name='register_program'),
    path('api/program/<slug:slug_name>', getProgramDetail, name='detail_program'),
    path('api/program/update/<slug:slug_name>', ProgramsList.as_view(), name='update_program'),
    path('api/program/delete/<slug:slug_name>', ProgramsList.as_view(), name='delete_program'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
