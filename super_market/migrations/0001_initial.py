# Generated by Django 5.0.3 on 2024-04-19 23:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

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
                (
                    "total_oreders",
                    models.DecimalField(
                        decimal_places=3, max_digits=10, verbose_name="اجمالي الفاتورة"
                    ),
                ),
            ],
            options={
                "verbose_name": "الاوردر",
                "verbose_name_plural": "الاوردر",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=200, verbose_name="اسم الصنف ")),
                (
                    "sell_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=6, verbose_name="سعر البيع "
                    ),
                ),
                (
                    "buy_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=6, verbose_name="سعر الشراء "
                    ),
                ),
                ("Quantity", models.PositiveBigIntegerField(verbose_name="الكميه")),
                (
                    "barcode",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        unique=True,
                        verbose_name="باركود",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "المنتج",
                "verbose_name_plural": "المنتج",
            },
        ),
        migrations.CreateModel(
            name="ProductHistory",
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
                ("name", models.CharField(max_length=200, verbose_name="اسم الصنف ")),
                (
                    "sell_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=6, verbose_name="سعر البيع "
                    ),
                ),
                (
                    "buy_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=6, verbose_name="سعر الشراء "
                    ),
                ),
                ("Quantity", models.PositiveBigIntegerField(verbose_name="الكميه")),
                (
                    "barcode",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        unique=True,
                        verbose_name="باركود",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "تتبع المنتجات",
                "verbose_name_plural": "تتبع المنتجات",
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("quantity", models.PositiveIntegerField(verbose_name="الكمية")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=3, max_digits=10, verbose_name="سعر البيع"
                    ),
                ),
                (
                    "total_cost",
                    models.DecimalField(
                        blank=True,
                        decimal_places=3,
                        max_digits=10,
                        null=True,
                        verbose_name="سعر الكمية",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="super_market.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="super_market.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "عناصر الاوردر ",
                "verbose_name_plural": "عناصر الاوردر",
            },
        ),
    ]
