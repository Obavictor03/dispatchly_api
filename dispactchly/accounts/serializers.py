from rest_framework import serializers
from .models import User, Sender, Rider


# Serializer for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'role', 'is_staff', 'is_active', 'date_joined']

    read_only_fields = ['id', 'is_staff', 'is_active', 'date_joined']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    

# Serializer for registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'role']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

# Serializer for Sender model
class SenderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Sender
        fields = ['id', 'user', 'business_name', 'phone_number', 'pickup_latitude', 'pickup_longitude', 'created_at']
        read_only_fields = ['id', 'created_at']


# Serializer for Rider model
class RiderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Rider
        fields = ['id', 'user', 'vehicle_type', 'license_plate', 'phone_number', 'created_at']
        read_only_fields = ['id', 'created_at']