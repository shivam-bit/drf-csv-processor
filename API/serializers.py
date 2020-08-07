from rest_framework import serializers
from .models import customer,csv_product,file_uploads

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields= ['id','name','email','created_date']
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = csv_product
        fields= ['id' , 'title','price','customer_id','uploaded_date']
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model= file_uploads
        fields= ['uploaded_by','file']
class DetailsSerializer(serializers.ModelSerializer):
    products=ProductSerializer(read_only=True, many=True)
    class Meta:
        model=customer
        fields=['id','name','email','created_date','products']