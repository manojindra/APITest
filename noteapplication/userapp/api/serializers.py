from rest_framework.serializers import ModelSerializer

from userapp.models import User

class UserSerailizer(ModelSerializer):

    class Meta: 
        model = User
        fields = ['username', 'email', 'firstName', 'lastName', 'password']

    def create(self, validated_data):

        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data, password= password)
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)

        if password:
            instance.set_password(password)
            instance.save()

        return instance
