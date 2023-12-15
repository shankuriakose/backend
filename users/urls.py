from django.urls import path 
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path ( '',get_routes),
    path('register', RegisterView.as_view()),
    path('me', RetrieveUserView.as_view()),
]
