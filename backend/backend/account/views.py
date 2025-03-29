from datetime import datetime

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserLoginSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        response = Response()
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)

            access_expiry = datetime.now() + settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
            refresh_expiry = datetime.now() + settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']
            response.set_cookie(
                key=settings.SIMPLE_JWT['ACCESS_TOKEN'],
                value=str(refresh.access_token),
                expires=access_expiry,
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            response.set_cookie(
                key=settings.SIMPLE_JWT['REFRESH_TOKEN'],
                value=str(refresh),
                expires=refresh_expiry,
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            response.data = {'is_admin': user.is_superuser}
            return response

        error_messages = []
        for field, errors in serializer.errors.items():
            error_messages.extend(errors)

        return Response({"message": error_messages[0]}, status=status.HTTP_400_BAD_REQUEST)

class TokenRefreshView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        print(request.data)
        return Response({'message': 'hi'}, status=status.HTTP_201_CREATED)

class HomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Hi"}, status=status.HTTP_200_OK)