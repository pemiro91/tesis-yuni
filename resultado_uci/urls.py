from django.urls import path

from resultado_uci.views import ResultadoList, getResultadoDetail

urlpatterns = [

    path('api/list', ResultadoList.as_view()),
    path('api/register', ResultadoList.as_view(), name='register_resultado'),
    path('api/<slug:slug_name>', getResultadoDetail, name='detail_resultado'),
    path('api/update/<slug:slug_name>', ResultadoList.as_view(), name='update_resultado'),
    path('api/delete/<slug:slug_name>', ResultadoList.as_view(), name='delete_resultado'),

]
