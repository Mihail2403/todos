from django.shortcuts import render
from rest_framework import response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .serializer import TODOSerializer
from .models import TODO


# Create your views here.
class TODOListAPIView(APIView):
    def get(self, request):
        print(request.user.id)
        todo = TODO.objects.filter(user_id=request.user.id)
        serializer = TODOSerializer(todo, many=True)
        return response.Response(serializer.data)

