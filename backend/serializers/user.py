from rest_framework import serializers

from backend.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name',
            'first_name',
            'last_name',
            'email',
            'avatar',
            'password'
        ]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': False
            },
            'avatar': {
                'required': False
            }
        }

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            instance.save()
        return instance
