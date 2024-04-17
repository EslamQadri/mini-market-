# Generated by Django 5.0.2 on 2024-02-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("super_market", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="products",
        ),
        migrations.AddField(
            model_name="orderitem",
            name="total_cost",
            field=models.DecimalField(decimal_places=3, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="order",
            name="number_of_order",
            field=models.CharField(default="qMAdPNopwQVGUy", max_length=50),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="price",
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]