# Generated by Django 5.0.3 on 2024-04-01 11:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("carts", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("cod", "Cod"),
                            ("card", "Card"),
                            ("paypal", "Paypal"),
                            ("other", "Other"),
                        ],
                        default="cod",
                        max_length=255,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("processing", "Processing"),
                            ("completed", "Completed"),
                            ("cancelled", "Cancelled"),
                            ("refunded", "Refunded"),
                            ("failed", "Failed"),
                            ("on_hold", "On Hold"),
                            ("shipped", "Shipped"),
                            ("delivered", "Delivered"),
                            ("returned", "Returned"),
                            ("exchanged", "Exchanged"),
                        ],
                        default="pending",
                        max_length=255,
                    ),
                ),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="carts.cart"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "orders",
            },
        ),
    ]
