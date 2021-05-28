# from django.urls import path
# from npo_jwt.views import NPOObtainTokenPairView
# from rest_framework_simplejwt.views import TokenRefreshView
#
#
# urlpatterns = [
#     path('login/', NPOObtainTokenPairView.as_view(), name='token_obtain_pair'),
#     path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]

from django.urls import path, include
from rest_framework import routers

from npo_jwt.views import NPOObtainTokenPairView, RegisterView, UserFilterSearch
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
router = routers.DefaultRouter()
router.register(r'', UserFilterSearch, 'filter')

urlpatterns = [
    path('login/', NPOObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('filter-user/', include(router.urls)),

]