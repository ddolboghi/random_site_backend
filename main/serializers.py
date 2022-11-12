from rest_framework import serializers
from .models import Alldata, Result

class AlldataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alldata
        fields = (
            'id',
            'is_choice',
            'question',
            'answer1',
            'answer2',
            'answer3',
        )

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = (
            'id',
            'content',
        )