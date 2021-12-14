from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')

    def validate(self, attrs):
        # here check password is strong or what! :D
        validate_password(attrs.get('password'))

        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError('Password and Confirm Password isn\'t equal!')

        return attrs

    def clean_validated_data(self):
        self.validated_data.pop('confirm_password')  # here delete confirm password because we dont need that
        return self.validated_data

    def create(self, validated_data):
        user = self.Meta.model.objects.create_user(**self.clean_validated_data())
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
