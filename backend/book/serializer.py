from rest_framework import serializers
from .models import BookModel


class BookSeializer(serializers.ModelSerializer):
    
    def get_author(self, obj):
        return {
            "username": obj.author.username,
            "first_name": obj.author.first_name,
            "last_name": obj.author.last_name
        }
        
    author = serializers.SerializerMethodField('get_author')

    class Meta:
        model = BookModel
        fields = '__all__'


class BookSeializerCreate(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'
