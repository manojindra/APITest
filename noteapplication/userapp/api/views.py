from rest_framework.generics import  CreateAPIView, RetrieveUpdateDestroyAPIView
from userapp.api.serializers import UserSerailizer
from userapp.models import User


class RegistrationView(CreateAPIView):
    serializer_class = UserSerailizer
    queryset = User.objects.all()

class UserUpdateView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = UserSerailizer
    lookup_field = 'username'
    queryset = User.objects.all()

