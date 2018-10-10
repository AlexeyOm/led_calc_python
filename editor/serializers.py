from rest_framework import serializers
from .models import Cabinet
class cabinet_serializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = '__all__'