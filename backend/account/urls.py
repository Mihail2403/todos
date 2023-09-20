from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from account.views import RegisterAPIView

acc_patterns = [
    path('reg/', RegisterAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='login'),

    # повторное получение refresh токена
    # страницы на фронте не должно существовать
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # страницы на фронте не должно существовать
    # проверка действителен ли access token
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]