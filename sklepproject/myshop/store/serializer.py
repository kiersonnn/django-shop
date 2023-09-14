from .models import Clothing,Rates
from rest_framework import serializers

class ClothingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Clothing
        fields=['type','name','description','name','price']

class RatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Rates
        fields=['clothing','rates','opinion']