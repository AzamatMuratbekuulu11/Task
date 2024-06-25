from rest_framework import serializers
from .models import *


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title_name', 'description', 'completed', 'created_date']