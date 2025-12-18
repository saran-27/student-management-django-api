from rest_framework.serializers import ModelSerializer
from .models import StudentPerformance

class Student_serializer(ModelSerializer):
    class Meta:
        model=StudentPerformance
        fields='__all__'