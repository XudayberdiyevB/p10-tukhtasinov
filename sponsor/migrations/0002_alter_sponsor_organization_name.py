# Generated by Django 4.2.3 on 2023-07-10 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sponsor", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sponsor",
            name="organization_name",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
