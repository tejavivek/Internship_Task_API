# Generated by Django 4.1 on 2023-12-22 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0002_rename_unit_pirce_invoicedetail_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicedetail',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
