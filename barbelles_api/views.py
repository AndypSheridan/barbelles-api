from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE, JWT_AUTH_SECURE
)


@api_view()
def root_route(request):
    return Response({
        'Message': 'Welcome to the BarBelles API, developed with Django Rest Framework'
        })
