from django.urls import path

from programs_uci.views import ProgramsList, getProgramDetail

urlpatterns = [

    path('api/list', ProgramsList.as_view()),
    path('api/register', ProgramsList.as_view(), name='register_program'),
    path('api/<slug:slug_name>', getProgramDetail, name='detail_program'),
    path('api/update/<slug:slug_name>', ProgramsList.as_view(), name='update_program'),
    path('api/delete/<slug:slug_name>', ProgramsList.as_view(), name='delete_program'),

]
