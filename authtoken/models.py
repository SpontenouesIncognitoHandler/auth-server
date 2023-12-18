from django.db import models
from uuid import uuid4
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from django.conf import settings

def generateUUID():
    return str(uuid4())

# Create your models here.


class Organization(models.Model):
    org_id = models.CharField(default=generateUUID, max_length=36, unique=True, editable=False,primary_key=True)
    email = models.EmailField(max_length=254)
    org_name = models.CharField(max_length=250)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.org_id

class UserRole(models.TextChoices):
    USER = 'user', 'User'
    AGENT = 'agent', 'Agent'

class User(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE,null=True)

    name = models.CharField(max_length=200)
    role = models.CharField(max_length=10, choices=UserRole.choices, default=UserRole.USER)
    user_token = models.TextField(blank=True, null=True)

    def generate_user_token(self):
        payload = {
            'user_id': self.id,
            'username': self.name,
            'organization_id': self.organization.org_id if self.organization else None,
            'role': self.role,
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        print(token)
        self.user_token = token
        self.save()

    def __str__(self):
        return self.name

