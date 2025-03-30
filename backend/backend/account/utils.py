from datetime import datetime

from django.conf import settings


def setCookies(response, access_token, refresh_token):

    access_expiry = datetime.now() + settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
    refresh_expiry = datetime.now() + settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']

    response.set_cookie(
        key=settings.SIMPLE_JWT['ACCESS_TOKEN'],
        value=str(access_token),
        expires=access_expiry,
        secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
        httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
        samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
    )
    response.set_cookie(
        key=settings.SIMPLE_JWT['REFRESH_TOKEN'],
        value=str(refresh_token),
        expires=refresh_expiry,
        secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
        httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
        samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
    )