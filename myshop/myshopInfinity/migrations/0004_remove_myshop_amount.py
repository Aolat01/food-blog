# Generated by Django 4.1.13 on 2025-04-12 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myshopInfinity", "0003_myshop_complete_payment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="myshop",
            name="Amount",
        ),
    ]
