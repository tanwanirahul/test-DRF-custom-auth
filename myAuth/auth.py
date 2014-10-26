'''
Created on 26-Oct-2014

@author: Rahul
'''
from rest_framework.authentication import BasicAuthentication
from myAuth.utils import get_scheme_key_value_authorization_tokens,\
    is_signature_valid
from django.contrib.auth.models import AnonymousUser
from rest_framework.exceptions import AuthenticationFailed


class SignedToken(BasicAuthentication):
    '''
        Our own implementation of Hashed Token based auth scheme.
    '''
    def authenticate(self, request):
        scheme, app_token, signature = get_scheme_key_value_authorization_tokens(request)  # @IgnorePep8

        print "scheme lower is %s " % (scheme.lower())

        if scheme.lower() not in ("token",):
            print "returning without computing token value"
            return None

        if is_signature_valid(request, signature, app_token):
            return AnonymousUser(), None
        else:
            raise AuthenticationFailed("Not a valid auth credentials")
