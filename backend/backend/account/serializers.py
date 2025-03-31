from django.conf import settings
from django.contrib.auth import get_user_model, authenticate
from rest_framework.fields import CharField
from rest_framework.exceptions import ValidationError
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
    def validate_email(self, value):
        if not UserModel.objects.filter(email=value).exists():
            raise ValidationError("User with this email does not exist.")


    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        elif user and not user.is_active:
            raise ValidationError('Account not active.')
        else:
            raise ValidationError('Incorrect credentials.')

class UserRegisterSerializer(Serializer):
    email = CharField()
    password = CharField(write_only=True, style={'input_type': 'password'})

    def validate_email(self, value):
        if UserModel.objects.filter(email=value).exists():
            raise ValidationError("A user with this email already exists.")
        return value

    def validate(self, data):
        user = UserModel.objects.create_user(**data)
        if user:
            return user
        return ValidationError("Invalid data")


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