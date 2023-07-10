from django.contrib.auth import login
from rest_framework import generics
from rest_framework.response import Response

from users.serializers import UserLoginSerializer


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        login(request, user)

        return Response(serializer.validated_data['tokens'])
