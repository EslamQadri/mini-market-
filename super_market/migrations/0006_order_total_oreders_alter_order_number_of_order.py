# Generated by Django 5.0.3 on 2024-04-14 00:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("super_market", "0005_alter_order_number_of_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="total_oreders",
            field=models.DecimalField(
                decimal_places=3,
                default=1,
                max_digits=10,
                verbose_name="اجمالي الفاتورة",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="order",
            name="number_of_order",
            field=models.CharField(
                default="kffmk4nd4ucn5t", max_length=50, verbose_name="الكود"
            ),
        ),
    ]