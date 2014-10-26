'''
Created on 26-Oct-2014

@author: Rahul
'''
from rest_framework import viewsets
from myAuth.models import Profile
from myAuth.serializers import ProfileSerializer, UserSerializer
from django.contrib.auth.models import User


class ProfileViewSet(viewsets.ModelViewSet):
    '''
        Viewset for profile model.
    '''
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    '''
        Viewset for profile model.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
