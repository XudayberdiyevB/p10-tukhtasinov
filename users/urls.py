from django.urls import path

from users.views import UserLoginAPIView, UserRegisterAPIView


urlpatterns = [
    path("register/", UserRegisterAPIView.as_view(), name="user-register"),
    path("login/", UserLoginAPIView.as_view(), name="user-login"),
]
