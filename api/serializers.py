from rest_framework import serializers
from . import models
from .models import Book , LibUser , RentBook , BookCategory

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class LibUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = LibUser
        fields = '__all__'


class RentBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentBook
        fields = '__all__'
        

class BookCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BookCategory
        fields = '__all__'
