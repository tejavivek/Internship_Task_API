from .views import *
from django.urls import path

urlpatterns = [
    path('invoices/', CreateInvoiceDetailView.as_view(), name = "invoices"),
    #path('invoices/<int:id>/', GetInvoiceDetailsView.as_view(), name = "invoices-id"),
    # path('invoices/<int:id>/', views.invoice_detail),
]
