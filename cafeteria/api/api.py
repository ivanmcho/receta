from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status

# API view para crear usuario tiene permiso para cualquiera pueda entrar
class UserAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data = request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

