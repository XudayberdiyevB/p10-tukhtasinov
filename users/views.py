from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import UserLoginSerializer, UserSerializer


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data["password"]
        hashed_password = make_password(password)
        serializer.save(password=hashed_password)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["username"], password=serializer.validated_data["password"]
        )
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({"access_token": str(refresh.access_token)})
        else:
            return Response({"error": "Incorrect username or password"}, status=status.HTTP_400_BAD_REQUEST)
