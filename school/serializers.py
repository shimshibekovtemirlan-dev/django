
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'login', 'email']



class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'login', 'email', 'password']

    def create(self, validated_data):

            print("REGISTER:", validated_data)

            return User.objects.create_user(
                login=validated_data['login'],
                email=validated_data['email'],
                password=validated_data['password']
            )

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

