from django.shortcuts import render
from rest_framework.views import APIView
#response will be given from Response function
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.
class SampleApiView(APIView):
    """The get method is responsible for handling the get requests"""
    def get(self,request,format=None):
        #Always response should be in the form of dictionary
        return Response({'name':"SampleAPIView",'message':"Hello World"})

    def post(self,request,format=None):
        return Response({'message':request.data,'request_method':"Post"})

    def put(self,request,format=None):
        return Response({'message':request.data,'request_method':"Put"})

    def patch(self,request,format=None):
        return Response({'message':request.data,'request_method':"Patch"})

    def delete(self,request,format=None):
        return Response({'message':"Deleted Successfully",'request_method':"Delete"})

class HelloViewset(viewsets.ViewSet):
    def list(self,request):
        message=[
            'it supports the methods such as list, create, retrieve, update, partial_update, destroy',
            'it supports the CRUD operations'
        ]
        return Response({'message':message})
