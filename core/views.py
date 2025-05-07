from django.shortcuts import render
from rest_framework.views import APIView

class LoginAPIView(APIView):
    def post(self, request):
        uname = request.data.get('username')
        pwd = request.data.get('password')
