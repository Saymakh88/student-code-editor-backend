from rest_framework import serializers
from .models import SavedCode

class SavedCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedCode
        fields = '__all__'
