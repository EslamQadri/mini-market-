from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from super_market.models import Product, ProductHistory


@receiver(post_save, sender=Product)
def tracking_products(sender, instance, created, **kwargs):
    if created:
        ProductHistory.objects.create(
            name=instance.name,
            sell_price=instance.sell_price,
            buy_price=instance.buy_price,
            Quantity=instance.Quantity,
            barcode=instance.barcode,
        )

    else:

        ProductHistory.objects.update_or_create(
            name=instance.name,
            barcode=instance.barcode,
            defaults={
                "name": instance.name,
                "sell_price": instance.sell_price,
                "buy_price": instance.buy_price,
                "Quantity": instance.Quantity,
            },
        )
