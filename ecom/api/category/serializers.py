from abc import ABCMeta

from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        file = ('name', 'description')
