from rest_framework import serializers
from main.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        ROLES = [
        ('admin', 'Administrator'),
        ('editor', 'Editor'),
        ('viewer', 'Viewer'),
        ]
        user = CustomUser(
            username=validated_data['username'],
            role=ROLES[2][0]
        )
        user.set_password(validated_data['password'])
        user.save()
        return user