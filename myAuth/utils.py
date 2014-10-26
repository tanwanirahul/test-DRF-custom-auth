'''
Created on 26-Oct-2014

@author: Rahul
'''
from rest_framework.exceptions import AuthenticationFailed
import md5
import hashlib
import base64
import hmac


def get_scheme_key_value_authorization_tokens(request):
    '''
        Given the request with AUTHRIZATION header as token apptoken:signature
        returns tuple of (token, apptoken, signature) authorization tokens.
    '''
    try:
        scheme, identity = request.META.get("HTTP_AUTHORIZATION").split(" ")
        app_token, signature = identity.split(":")
        return (scheme, app_token, signature)

    except Exception as e:
        raise AuthenticationFailed("Unable to parse the AUTHORIZATION header")


def get_string_to_sign(request):
    '''
        Returns a string that needs to be signed for making this request
    '''
    return "\n".join([
        request.method.upper(), md5.new(request.body).hexdigest(),
        request.content_type,
        request.META.get("HTTP_X_DATE"),
        request.build_absolute_uri(request.path)
    ])


def compute_signature_token_string(string_to_sign, secret_key):
    '''
        Computes the signature for the given string using the given secret.
    '''
    return base64.b64encode(hmac.new(secret_key, string_to_sign.encode("utf-8"), hashlib.sha1).digest())  # @IgnorePep8


def is_signature_valid(request, signature, app_secret="demo_secret"):  # @IgnorePep8
    '''
        Returns if the signature is valid.
    '''
    string_to_sign = get_string_to_sign(request)
    print "string is %s " % (string_to_sign)
    computed_sign = compute_signature_token_string(string_to_sign, app_secret)  # @IgnorePep8
    print "Computed hash %s " % (computed_sign)
    return signature == computed_sign
