from django.db import models

# Create your models here.

class Invoice(models.Model):
    Date=models.DateField()
    Customer_Name=models.CharField(max_length=200)

    def __str__(self):
        return f"Invoice #{self.id}-{self.Customer_Name}"

class InvoiceDetail(models.Model):
    invoice=models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='details')
    Description=models.CharField(max_length=255)
    quantity=models.PositiveIntegerField()
    unit_price= models.DecimalField(max_digits=10, decimal_places=2)
    price=models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    

    def save(self, *args,  **kwargs):
         self.price=self.quantity * self.unit_price 
         super().save(*args, **kwargs)

    def __str__(self):
            return f"Detail for Invoice #{self.invoice.pk} - {self.Description}- "


    