# Generated by Django 5.1.7 on 2025-04-01 16:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("outward_supply", "0007_alter_retailer_total_sales"),
    ]

    operations = [
        migrations.AlterField(
            model_name="retailer",
            name="phone_number",
            field=models.CharField(
                max_length=10,
                validators=[django.core.validators.MinLengthValidator(10)],
            ),
        ),
    ]
