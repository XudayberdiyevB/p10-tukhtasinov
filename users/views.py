from django.contrib.auth import login
from rest_framework import generics
from rest_framework.response import Response

from users.serializers import UserLoginSerializer, UserSerializer


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        login(request, user)
        tokens = serializer.validated_data["tokens"]
        user_data = UserSerializer(user).data

        response_data = {"tokens": tokens, "user": user_data}

        return Response(response_data)
