# Generated by Django 5.1.6 on 2025-03-24 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outward_supply', '0002_outward_invoice_productentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productentry',
            name='amount',
            field=models.FloatField(),
        ),
    ]
