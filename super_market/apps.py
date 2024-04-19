from django.apps import AppConfig


class SuperMarketConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "super_market"

    def ready(self):
        import super_market.signals
