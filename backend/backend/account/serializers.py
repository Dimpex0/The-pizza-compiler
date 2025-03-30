from django.conf import settings
from django.contrib.auth import get_user_model, authenticate
from rest_framework.fields import CharField
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework_simplejwt.tokens import RefreshToken

UserModel = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'email', 'is_active']

class UserLoginSerializer(Serializer):
    email = CharField()
    password = CharField(write_only=True, style={'input_type': 'password'})

    # TODO: run field validations and raise custom errors

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        elif user and not user.is_active:
            raise ValidationError('Account not active.')
        else:
            raise ValidationError('Incorrect credentials.')

class TokenRefreshSerializer(Serializer):
    def validate(self, data):
        request = self.context.get('request')
        refresh_token = request.COOKIES.get(settings.SIMPLE_JWT["REFRESH_TOKEN"])
        if refresh_token:
            try:
                new_refresh_token = RefreshToken(refresh_token)
                new_access_token = str(new_refresh_token.access_token)
                return {"new_refresh_token": new_refresh_token, "new_access_token": new_access_token}
            except Exception:
                pass
        raise ValidationError("Error refreshing access token. Login required.")

# Response({'error': "Couldn't refresh access token. Login required."}, status=status.HTTP_400_BAD_REQUEST)