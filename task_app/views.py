from django.shortcuts import render
from .models import Invoice,InvoiceDetail
from .serializers import InvoiceSerializer,InvoiceDataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET','POST'])
def  Invoice_index(request):

    if request.method =='GET':
        Invoices=Invoice.objects.all()
        serializer=InvoiceSerializer(Invoices, many=True)
        return Response(serializer.data)

    if request.method=='POST':
        serializer=InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])

def invoice_detail(request, id, format=None):
     try:
         Invoice=InvoiceDetail.objects.get(pk=id)
     except Invoice.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)
     
     if request.method == 'GET':
         serializer = InvoiceDataSerializer(Invoice)
         return Response(serializer.data)

     if request.method =='PUT':
         serializer = InvoiceDataSerializer(Invoice, data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
     elif request.method =='DELETE':
        Invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
