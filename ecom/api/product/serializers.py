from rest_framework import serializers
from .models import Product


class CategorySerializer(serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Product
        fields = ('name', 'description')