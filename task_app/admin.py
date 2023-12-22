from django.contrib import admin
from .models import  Invoice,InvoiceDetail

admin.site.register(Invoice)
admin.site.register(InvoiceDetail)

# Register your models here.
