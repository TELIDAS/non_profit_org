# from django.urls import path
# from npo_jwt.views import NPOObtainTokenPairView
# from rest_framework_simplejwt.views import TokenRefreshView
#
#
# urlpatterns = [
#     path('login/', NPOObtainTokenPairView.as_view(), name='token_obtain_pair'),
#     path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]

from django.urls import path
from npo_jwt.views import NPOObtainTokenPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('login/', NPOObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]