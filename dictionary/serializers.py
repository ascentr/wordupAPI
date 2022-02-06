from rest_framework import serializers
from dictionary.models import Words

#word serializer
class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = '__all__'
