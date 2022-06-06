from dataclasses import fields
from pyexpat import model
from numpy import source
from rest_framework import serializers
from django.contrib.auth.models import User
from loginpage.models import Profile, Tweet


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class ProfileSerializer(serializers.ModelSerializer):
    user_one = UserSerializer(read_only=True,source='user')
    class Meta:
        model = Profile
        fields = ('user', 'gender', 'age', 'description', 'user_one')
        # depth = 1

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = "__all__"