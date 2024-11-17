from django.urls import path

from comite_uci.views import ComiteList, getComiteDetail, getComiteForEvent

urlpatterns = [

    path('api/list/<slug:slug_event>', getComiteForEvent, name='list_comite'),
    path('api/register', ComiteList.as_view(), name='register_comite'),
    path('api/<slug:slug_name>', getComiteDetail, name='detail_comite'),
    path('api/update/<slug:slug_name>', ComiteList.as_view(), name='update_comite'),
    path('api/delete/<slug:slug_name>', ComiteList.as_view(), name='delete_comite'),

]
