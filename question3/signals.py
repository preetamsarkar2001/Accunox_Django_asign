
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from django.test import TestCase
from .models import TestModel

@receiver(post_save, sender=TestModel)
def test_signal_in_transaction(sender, instance, **kwargs):
 
    in_transaction = transaction.get_connection().in_atomic_block
    print(f"Signal handler in transaction: {in_transaction}")
