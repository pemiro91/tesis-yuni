from equipo_uci.views import EquipoList, getEquipoDetail
from django.urls import path

urlpatterns = [

    path('api/list', EquipoList.as_view()),
    path('api/register', EquipoList.as_view(), name='register_equipo'),
    path('api/<slug:slug_name>', getEquipoDetail, name='detail_equipo'),
    path('api/update/<slug:slug_name>', EquipoList.as_view(), name='update_equipo'),
    path('api/delete/<slug:slug_name>', EquipoList.as_view(), name='delete_equipo'),

]
