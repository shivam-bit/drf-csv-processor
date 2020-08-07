from django.shortcuts import render
from .models import customer,csv_product,file_uploads
from .serializers import CustomerSerializer,ProductSerializer,FileSerializer,DetailsSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework import serializers
import csv,io
from rest_framework.response import Response
from rest_framework import status

# customer view to get all customers and to create new customer
class CustomerView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class = CustomerSerializer
    queryset =  customer.objects.all()
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

# product view to manually add a single product to csv_product model
class ProductView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class = ProductSerializer
    queryset =  csv_product.objects.all()
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

# file upload view to process csv_file
class FileUploadView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class = FileSerializer
    queryset =  file_uploads.objects.all()
    def ConvertStringToList(self,string): 
            li = list(string.split('\n')) 
            return li 
    def SplitByField(self,string):
            li = list(string.split(',')) 
            return li 
    def fileProcessor(self,data_set,customerId):
        data_set=(self.ConvertStringToList(data_set))
        for item in data_set[1:]:
            item=self.SplitByField(item)
            while len(item)>2:
                item[0]+=","+item.pop(1)
            item[1]=float(item[1])
            productInstance=csv_product(title=item[0],price=item[1],customer_id=customerId)
            productInstance.save()
    def get(self,request):
        return self.list(request)
    def post(self,request):
        a=customer.objects.get(pk=request.data['uploaded_by'])
        csv_file = request.FILES['file']
        # checks whether csv file is uploaded or not
        if not csv_file.name.endswith('.csv'):
            return Response({'message':'THIS IS NOT A CSV FILE'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        data_set = csv_file.read().decode('UTF-8')
        # sends file for processing
        self.fileProcessor(data_set,a)
        return self.create(request)

# access customer details and all the products he uploaded in latest order
class CustomerDetailView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class = DetailsSerializer
    queryset= customer.objects.all()
    lookup_field='id'
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
