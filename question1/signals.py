# signals_test/signals.py
from django.dispatch import Signal, receiver
import time

# Define a custom signal
my_signal = Signal()

# Signal handler to simulate a time-consuming task
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print("Signal handler started.")
    time.sleep(5)  # Simulate a long-running process
    print("Signal handler finished.")
