from django.contrib.auth import get_user_model, authenticate
from rest_framework.fields import CharField
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, Serializer

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