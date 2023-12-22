from rest_framework import serializers
from .models import Invoice
from .models import InvoiceDetail



class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Invoice
        fields =['id','Date', 'Customer_Name']

class InvoiceDataSerializer(serializers.ModelSerializer):
     class Meta:
         model= InvoiceDetail
         fields =['id','invoice','Description','quantity','unit_price','price']
         
