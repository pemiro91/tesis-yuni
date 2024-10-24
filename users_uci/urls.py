from django.urls import path
from django.urls.conf import include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from users_uci.views import UserApi, getProfile

urlpatterns = [

    path('api-auth/', include('rest_framework.urls')),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view()),

    path('api/list', UserApi.as_view(), name='users'),
    path('api/register', UserApi.as_view(), name='register_user'),
    path('api/profile', getProfile, name='profile'),
    path('api/update/<slug:slug_username>', UserApi.as_view(), name='profile_update'),
    path('api/delete/<slug:slug_username>', UserApi.as_view(), name='delete_user'),

]
