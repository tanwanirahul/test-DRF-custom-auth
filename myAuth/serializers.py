'''
Created on 26-Oct-2014

@author: Rahul
'''
from rest_framework import serializers
from myAuth.models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    '''
        Profile Serializer
    '''

    class Meta:
        '''
            Meta options.
        '''
        model = Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    '''
        Profile Serializer
    '''

    class Meta:
        '''
            Meta options.
        '''
        model = User
