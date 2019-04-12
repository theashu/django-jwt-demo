from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.utils.translation import ugettext as _

from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER
class UserCreateSerializer(ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields=[
            'profile_photo',
            'username',
            'password',
            'email',
            'name',
            'platform',
            'phone',
            'token',
        ]
        extra_kwargs = {"password":{"write_only":True}}


    def get_token(self,user):
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise serializers.ValidationError(msg)
            payload = jwt_payload_handler(user)
            return jwt_encode_handler(payload)
        else:
            msg = _('Unable to log in.')
            raise serializers.ValidationError(msg)
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        user.token = "dfd"
        return user
    
    def validate(self,data):
        username=data['username']
        email=data['email']
        user_un= User.objects.filter(username=username)
        user_em= User.objects.filter(email=email)
        if user_un.exists():
            raise ValidationError("Username already exits")
        if user_em.exists():
            raise ValidationError("Email already exits")
        return data
    
class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields=[
            'profile_photo',
            'username',
            'email',
            'name',
            'platform',
            'phone',
        ]