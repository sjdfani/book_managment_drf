from rest_framework import serializers
from .models import BookModel
from django.contrib.auth import get_user_model


class AuthorSeri(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class BookSeializer(serializers.ModelSerializer):
    # def get_author(self, obj):
    #     return {
    #         "username": obj.author.username,
    #         "first_name": obj.author.first_name,
    #         "last_name": obj.author.last_name
    #     }
        
    # author = serializers.SerializerMethodField('get_author')
    # author = AuthorSeri()
    class Meta:
        model = BookModel
        fields = '__all__'
        
    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['author'] = AuthorSeri(instance.author).data
        return res

class BookSeializerCreate(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'
