from django.db import models
from super_market.utiltes import random_code
from django.core.exceptions import ValidationError


# Create your models here.
class Product(models.Model):
    name = models.CharField("اسم الصنف ", max_length=200)
    sell_price = models.DecimalField("سعر البيع ", max_digits=6, decimal_places=2)
    buy_price = models.DecimalField("سعر الشراء ", max_digits=6, decimal_places=2)
    Quantity = models.PositiveBigIntegerField(
        "الكميه",
    )
    # make bar code unice
    barcode = models.CharField(
        "باركود", max_length=50, blank=True, null=True, unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.Quantity < 0:
            raise ValidationError(
                f" عدد المنتاجات {self.name}اقل من العدد الموجود فى المحل "
            )
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "المنتج"
        verbose_name_plural = "المنتج"


class ProductHistory(Product):
    pass


class Order(models.Model):
    """
    the name of bill is the id
    """

    created_at = models.DateTimeField(auto_now_add=True)
    total_oreders = models.DecimalField(
        "اجمالي الفاتورة", max_digits=10, decimal_places=3
    )

    def __str__(self) -> str:
        return f"{self.pk } {self.total_oreders}"

    class Meta:
        verbose_name = "الاوردر"
        verbose_name_plural = "الاوردر"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("الكمية")
    price = models.DecimalField("سعر البيع", max_digits=10, decimal_places=3)
    total_cost = models.DecimalField(
        "سعر الكمية", max_digits=10, decimal_places=3, blank=True, null=True
    )

    def save(self, *args, **kwargs):
        if self.quantity > self.product.Quantity:
            raise ValidationError(
                f" عدد   {self.product.name } اقل من العدد الموجود فى المحل    "
            )
        if self.price < self.product.buy_price:
            raise ValidationError("كدا احنا بنخسر سعر البيع اقل من سهر الشراء ")
        self.total_cost = self.quantity * self.price
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f" {self.pk} { self.total_cost}"

    class Meta:
        verbose_name = "عناصر الاوردر "
        verbose_name_plural = "عناصر الاوردر"
