# question2/signals.py
from django.dispatch import Signal, receiver
import threading

# Define a custom signal
signal_for_thread_test = Signal()

# Signal handler to check thread identity
@receiver(signal_for_thread_test)
def signal_handler(sender, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")
