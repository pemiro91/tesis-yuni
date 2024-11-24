from django.urls import path

from evidencia_uci.views import getEvidenciaDetail, EvidenciaList, getListEvidenciaForUser

urlpatterns = [

    path('api/list', EvidenciaList.as_view()),
    path('api/register', EvidenciaList.as_view(), name='register_evidencia'),
    path('api/<slug:slug_name>', getEvidenciaDetail, name='detail_evidencia'),
    path('api/update/<slug:slug_name>', EvidenciaList.as_view(), name='update_evidencia'),
    path('api/delete/<slug:slug_name>', EvidenciaList.as_view(), name='delete_evidencia'),
    path('api/list_user', getListEvidenciaForUser, name='list_evidencia_user'),

]
