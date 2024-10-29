from django.urls import path

from comite_uci.views import ComiteList, getComiteDetail

urlpatterns = [

    path('api/list', ComiteList.as_view()),
    path('api/register', ComiteList.as_view(), name='register_comite'),
    path('api/<slug:slug_name>', getComiteDetail, name='detail_comite'),
    path('api/update/<slug:slug_name>', ComiteList.as_view(), name='update_comite'),
    path('api/delete/<slug:slug_name>', ComiteList.as_view(), name='delete_comite'),

]
