from rest_framework import serializers
from .models import TODO

class TODOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields = ['id', 'text', 'user_id']
