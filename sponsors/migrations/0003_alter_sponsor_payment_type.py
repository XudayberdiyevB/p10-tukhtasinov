# Generated by Django 4.2.3 on 2023-07-13 10:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sponsors", "0002_sponsor_payment_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sponsor",
            name="payment_type",
            field=models.CharField(
                choices=[("cash", "Cash"), ("card", "Card"), ("transfer", "Transfer")],
                max_length=8,
            ),
        ),
    ]
