from django.urls import path

from users.views import UserLoginAPIView, UserRegisterView


urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path("login/", UserLoginAPIView.as_view(), name="user-login"),
]
