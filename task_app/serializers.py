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
         
class GetInvoiceDetailsSerializer(serializers.ModelSerializer):
    customer_details = serializers.SerializerMethodField()
    class Meta:
        model= InvoiceDetail
        fields =['id','customer_details','Description','quantity','unit_price','price']
    def get_customer_details(self, obj):
        try:
            customer = Invoice.objects.get(id = obj.invoice_id)
            serializer = InvoiceSerializer(customer)
            return serializer.data
        except Exception as error:
            return obj.invoice_id