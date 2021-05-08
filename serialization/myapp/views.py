from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from myapp.serializers import HelloSerializer
# Create your views here.
class HelloApiView(APIView):
    serializer_class=HelloSerializer
    """The Get method is responsible for handling the Get requests"""
    def get(self,request,format=None):
        #always the response should be in the form of dictionary.
        return Response({'message':'Welcome to 1st Api','request_type':'Get'})
    
    def post(self,request,format=None):
        serializer_class_instance=self.serializer_class(data=request.data)
        if serializer_class_instance.is_valid():
            data=serializer_class_instance.validated_data
        return Response({'message':'Welcome to 1st Api','request_type':'Post','data':data})
   
    def put(self,request,format=None):
        serializer_class_instance=self.serializer_class(data=request.data)
        if serializer_class_instance.is_valid():
            data=serializer_class_instance.validated_data
        return Response({'message':'Welcome to 1st Api','request_type':'Put','data':data})

    def patch(self,request,format=None):
        serializer_class_instance=self.serializer_class(data=request.data)
        if serializer_class_instance.is_valid():
            data=serializer_class_instance.validated_data
        return Response({'message':'Welcome to 1st Api','request_type':'Patch','data':data})

    def delete(self,request,format=None):
        return Response({'message':'Welcome to 1st Api','request_type':'Delete'})


#Method 2 : Interfacing the API with db through Serializers 
"""The below class method is to interfacing the API with db through Serializers using \
    Http GET and POST request methods – It includes models.py and admin.py files too.  \
        This is not a different topic and hint has been mentioned for my reference."""

from serializers.models import SampleModel

class HelloApiView_1(APIView):
    serializer_class=HelloSerializer
    """The Get method is responsible for handling the Get requests"""
    def get(self,request,format=None):
        #always the response should be in the form of dictionary.
        data=SampleModel.objects.values() #will give u all the data in dictionary format
        return Response({'message':'Welcome to 1st Api','request_type':'Get','data':data})
    
    def post(self,request,format=None):
        serializer_class_instance=self.serializer_class(data=request.data)
        if serializer_class_instance.is_valid():
            data=serializer_class_instance.validated_data
            user=SampleModel.objects.get_or_create(name=data['name'],email=data['email'],gender=data['gender'])
        return Response({'message':'Welcome to 1st Api','request_type':'POST','data':data})


#Method 3 : Getting/Displaying the record Using Primary Key
"""The below class method is to getting/displaying the record from backend(DB) to frontend \
    with the primary key attribute using the Http GET request method/function"""

class HelloApiView_2(APIView):
    serializer_class=HelloSerializer
    """The Get method is responsible for handling the Get requests"""
    def get(self,request,pk=None,format=None):
        #always the response should be in the form of dictionary.
        if pk==None:
            data=SampleModel.objects.values()
        else:
            data=SampleModel.objects.filter(id=pk).values()#will give u all the data in dictionary format
        return Response({'message':'Welcome to 1st Api','request_type':'Get','data':data})

