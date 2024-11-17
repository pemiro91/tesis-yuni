from django.urls import path

from resultado_uci.views import ResultadoList, getListResultadoForEvent

urlpatterns = [

    path('api/list', ResultadoList.as_view(), name='list_resultado'),
    path('api/register', ResultadoList.as_view(), name='register_resultado'),
    path('api/update/<slug:slug_name>', ResultadoList.as_view(), name='update_resultado'),
    path('api/delete/<slug:slug_name>', ResultadoList.as_view(), name='delete_resultado'),
    path('api/event/<slug:slug_event>', getListResultadoForEvent, name='list_for_event_resultado'),

]
