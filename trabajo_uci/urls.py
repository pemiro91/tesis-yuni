from django.urls import path

from trabajo_uci.views import TrabajoList, getTrabajoDetail

urlpatterns = [

    path('api/list', TrabajoList.as_view()),
    path('api/register', TrabajoList.as_view(), name='register_trabajo'),
    path('api/<slug:slug_name>', getTrabajoDetail, name='detail_trabajo'),
    path('api/update/<slug:slug_name>', TrabajoList.as_view(), name='update_trabajo'),
    path('api/delete/<slug:slug_name>', TrabajoList.as_view(), name='delete_trabajo'),

]
