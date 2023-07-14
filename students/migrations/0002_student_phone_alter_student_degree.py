# Generated by Django 4.2.3 on 2023-07-12 13:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="phone",
            field=models.CharField(default="", max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="student",
            name="degree",
            field=models.CharField(
                choices=[("bachelors", "Bachelors"), ("master", "Master")],
                max_length=50,
            ),
        ),
    ]
