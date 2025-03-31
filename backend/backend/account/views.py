from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserLoginSerializer, TokenRefreshSerializer, UserRegisterSerializer
from .utils import setCookies


class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        response = Response()
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)

            setCookies(response, refresh.access_token, refresh)

            response.data = {'is_admin': user.is_superuser}
            return response

        error_messages = []
        for field, errors in serializer.errors.items():
            error_messages.extend(errors)

        return Response({"message": error_messages[0]}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():

            # TODO: Send an activation link

            return Response({'message': "Account created successfully. We've sent an activation link to your email."},
                            status=status.HTTP_201_CREATED)

        error_messages = []
        for field, errors in serializer.errors.items():
            error_messages.extend(errors)

        return Response({"message": error_messages[0]}, status=status.HTTP_400_BAD_REQUEST)

class TokenRefreshView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        serializer = TokenRefreshSerializer(data=request.data, context={"request": request})
        response = Response()
        if serializer.is_valid():
            new_access_token = serializer.validated_data.get('new_access_token')
            new_refresh_token = serializer.validated_data.get('new_refresh_token')
            setCookies(response, new_access_token, new_refresh_token)
            response.status_code = status.HTTP_200_OK
            return response
        else:
            return Response({"message": "Couldn't refresh access token. Login required."},
                            status=status.HTTP_400_BAD_REQUEST)