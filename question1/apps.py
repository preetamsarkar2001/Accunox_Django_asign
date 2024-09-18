from django.apps import AppConfig


class Question1Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "question1"
    def ready(self):
        # Import signals when the app is ready
        from . import signals
