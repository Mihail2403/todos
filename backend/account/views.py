from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import views, response


# Create your views here.
class RegisterAPIView(views.APIView):

    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
            email = request.data['email']
            user = User.objects.create_user(username=username, password=password, email=email)
            return response.Response({"status": "good", "user_id": user.id})
        except:
            return response.Response({"status": "bad"})