from django.shortcuts import render
from .models import Invoice,InvoiceDetail
from .serializers import InvoiceSerializer,InvoiceDataSerializer, GetInvoiceDetailsSerializer
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class CreateInvoiceDetailView(APIView):
    def post(self, request):
        invoice_serializer = InvoiceSerializer(data = {"Customer_Name": request.data["Customer_Name"]})
        if invoice_serializer.is_valid():
            invoice_serializer.save()
        else:    
            return Response({"data": invoice_serializer.errors, "message": "Something went wrong", "code":status.HTTP_400_BAD_REQUEST})
        request.data["invoice"] = invoice_serializer.data["id"]    
        invoice_details_serializer = InvoiceDataSerializer(data = request.data)
        if invoice_details_serializer.is_valid():
            invoice_details_serializer.save()
            return Response({"data": invoice_details_serializer.data, "message": "Invoice details added successfully", "code":status.HTTP_201_CREATED})
        return Response({"data": invoice_details_serializer.errors, "message": "Something went wrong", "code":status.HTTP_400_BAD_REQUEST})
    
    def get(self, request):
        all_invoice_details = InvoiceDetail.objects.all()
        serializer = GetInvoiceDetailsSerializer(all_invoice_details, many=True)
        return Response({"data": serializer.data, "message": "All records fetched successfully", "code":status.HTTP_200_OK})



class GetInvoiceDetailsView(APIView):
    def get(self, request, id):
        try:
            get_invoice_details = InvoiceDetail.objects.get(id = id)
        except:
            return Response({"data": None, "message": "Record not found", "code":status.HTTP_400_BAD_REQUEST})
        serializer = GetInvoiceDetailsSerializer(get_invoice_details)
        return Response({"data": serializer.data, "message": "Invoice details fetched successfully", "code":status.HTTP_200_OK})
    
    def put(self, request, id):
        try:
            get_invoice_details = InvoiceDetail.objects.get(id = id)
        except:
            return Response({"data": None, "message": "Record not found", "code":status.HTTP_400_BAD_REQUEST})
        request.data["invoice"] = get_invoice_details.invoice_id    
        serializer = InvoiceDataSerializer(get_invoice_details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "Invoice details updated successfully", "code":status.HTTP_200_OK})
        return Response({"data": serializer.errors, "message": "Something went wrong", "code":status.HTTP_400_BAD_REQUEST})

    def delete(self, request, id):
        try:
            get_invoice_details = Invoice.objects.get(id = id)
            get_invoice_details.delete()
            return Response({"data": None, "message": "Invoice deleted successfully", "code":status.HTTP_200_OK})
        except:
            return Response({"data": None, "message": "Record not found", "code":status.HTTP_400_BAD_REQUEST})

















# @api_view(['GET','POST'])
# def  Invoice_index(request):

#     if request.method =='GET':
#         Invoices=Invoice.objects.all()
#         serializer=InvoiceSerializer(Invoices, many=True)
#         return Response(serializer.data)

#     if request.method=='POST':
#         serializer=InvoiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
# @api_view(['GET','PUT','DELETE'])

# def invoice_detail(request, id, format=None):
#      try:
#         Invoice=InvoiceDetail.objects.get(pk=id)
#      except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
     
#      if request.method == 'GET':
#          serializer = InvoiceDataSerializer(Invoice)
#          return Response(serializer.data)

#      if request.method =='PUT':
#          serializer = InvoiceDataSerializer(Invoice, data=request.data)
#          if serializer.is_valid():
#              serializer.save()
#              return Response(serializer.data)
#          else:
#              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#      elif request.method =='DELETE':
#         Invoice.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

