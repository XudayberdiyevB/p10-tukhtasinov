from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from .serializers import SponsorSerializer


class SponsorApi(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SponsorSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
