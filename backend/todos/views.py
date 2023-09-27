
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .serializer import TODOSerializer
from .models import TODO


# Create your views here.
class TODOListAPIView(APIView):
    def get(self, request):
        try:
            print(request.user)
            todo = TODO.objects.filter(user_id=request.user.id)
            serializer = TODOSerializer(todo, many=True)
            return response.Response(serializer.data)
        except Exception as e:
            print(e)
            return response.Response({"status":"bad"})
    
    def post(self, request):
        try:
            if TODO.objects.filter(text=request.data['text'], user=User.objects.get(id=request.user.id)).exists():
                return response.Response({"status":"good"})
            else:
                todo = TODO(text=request.data['text'], user=User.objects.get(id=request.user.id))
                todo.save()
                return response.Response({"status":"good", "todo_id":todo.id})
        except Exception as e:
           print(e)
           return response.Response({"status":"bad"})
        
class DeleteTODOAPIView(APIView):
     def post(self, request):
        try:
            todo = TODO.objects.get(text=request.data['text'], user=User.objects.get(id=request.user.id))
            todo.delete()
            return response.Response({"status": "good", "del_todo_id": todo.id})
        except Exception as e:
            print(e)
            return response.Response({"status": "bad"})
