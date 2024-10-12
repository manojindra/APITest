from django.urls import path
from userapp.api.views import RegistrationView, UserUpdateView

urlpatterns = [
     path('register/', RegistrationView.as_view()), 
     path('user/<str:username>/', UserUpdateView.as_view() )

]
