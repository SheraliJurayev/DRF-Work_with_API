from django.shortcuts import render
from rest_framework import viewsets
from api.models import Book , LibUser , RentBook
from api.serializers import BookSerializer , LibUserSerializer , RentBookSerializer
from rest_framework.response import Response
from .pagination import CustomPagination


# viewset = list ,  create , retrieve ,  update , delete ,partial_update , destroy ,


class BookViewSet(viewsets.ViewSet):
    def list(self  ,request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset , many=True)
        return Response(serializer.data)
    
    def post(self , request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        return Response(serializer.errors )






class LibUserViewSet(viewsets.ModelViewSet):
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer
    pagination_class = CustomPagination

class RentBookViewSet(viewsets.ModelViewSet):
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer       

