# Generated by Django 5.0.3 on 2024-04-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carts", "0002_alter_cart_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="status",
            field=models.CharField(
                choices=[("open", "Open"), ("closed", "Closed")],
                default="open",
                max_length=16,
            ),
        ),
    ]