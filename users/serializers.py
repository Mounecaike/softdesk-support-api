from rest_framework import serializers
from datetime import date
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'date_of_birth',
            'can_be_contacted',
            'can_data_be_shared',
            'created_time',
            'password'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_date_of_birth(self, value):
        today = date.today()
        age = today.year - value.year
        if (today.month, today.day) < (value.month, value.day):
            age -= 1

        if age < 15:
            raise serializers.ValidationError(
                "L'utilisateur doit avoir au moins 15 ans pour s'inscrire."
            )

        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
