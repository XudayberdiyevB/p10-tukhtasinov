# Generated by Django 4.2.3 on 2023-07-12 12:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="phone",
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
