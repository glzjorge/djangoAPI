from rest_framework import serializers
from categories.models import Category

class CatergorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug', 'published']

