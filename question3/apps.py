from django.apps import AppConfig


class Question3Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "question3"
    def ready(self):
        from . import signals
