# Generated by Django 5.1.6 on 2025-03-24 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inward_supply', '0005_alter_invoicebill_bill_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicebill',
            name='bill_number',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email_id',
            field=models.EmailField(max_length=254),
        ),
    ]
