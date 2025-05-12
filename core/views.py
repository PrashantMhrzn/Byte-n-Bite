from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.serializers import ValidationError
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class LoginAPIView(APIView):
    def post(self, request):
        uname = request.data.get('username')
        pwd = request.data.get('password')
        if uname == None and pwd == None:
            raise ValidationError({
                "Detail": "Both username and password are requried!"
            })
        user = authenticate(username = uname, password = pwd)
        if user:
            # gives token and bool, and get or create creates if no user token, gets if user token previously available
            token,_=Token.objects.get_or_create(user = user)
            return Response({
                "token": token.key,
                "user": user.username
            })
        return Response({
            "details": "User is not valid!"
        })

