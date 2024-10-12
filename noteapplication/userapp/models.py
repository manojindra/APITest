import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator

# Create your models here.

class UserManger(BaseUserManager):

    def create_superuser(self, username, email, password):

        superuser = self.model(username=username, email= self.normalize_email(email))
        superuser.set_password(password)
        superuser.is_active = True
        superuser.is_superuser = True
        superuser.is_staff = True
        
        superuser.save(using=self.db)

        return superuser


    def create_user(self, username, email, password, **extra_fileds):

        user = self.model(username= username, email=self.normalize_email(email), **extra_fileds)
        user.set_password(password)
        user.is_active = True
        user.save(using=self.db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    
    userid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, null=False)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True, null=False, blank=False, validators=[EmailValidator])
    firstName = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    password = models.CharField(validators=[MinLengthValidator(8), MaxLengthValidator(16)])
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS= ['email']

    objects = UserManger()
    

    def __str__(self):
        return self.username



