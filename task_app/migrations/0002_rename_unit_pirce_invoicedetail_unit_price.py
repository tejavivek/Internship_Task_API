# Generated by Django 4.2.8 on 2023-12-22 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoicedetail',
            old_name='unit_pirce',
            new_name='unit_price',
        ),
    ]
