

```markdown
# Questions for Django Trainee at Accuknox

## Topic: Django Signals

### Question 1: By default, are Django signals executed synchronously or asynchronously?
Please support your answer with a code snippet that conclusively proves your stance.

**Answer**: By default, Django signals are executed synchronously. This means that when a signal is sent, the connected signal handlers run immediately in the same thread that triggered the signal.

#### Example:

```python
from django.dispatch import Signal, receiver
import time

# Define a custom signal
my_signal = Signal()

# Receiver function to handle the signal
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print("Signal handler started.")
    time.sleep(5)  # Simulate a delay
    print("Signal handler finished.")

# Function to trigger the signal
def trigger_signal():
    print("Before signal.")
    my_signal.send(sender=None)  # Trigger the signal
    print("After signal.")

# Trigger the signal
trigger_signal()
```

#### Output:

```
Before signal.
Signal handler started.
<5-second delay>
Signal handler finished.
After signal.
```

This proves that signals are executed synchronously.

![Question 1 Image](https://github.com/user-attachments/assets/62f5aa96-0abd-45c3-a351-51eab3d73cab)

---

### Question 2: Do Django signals run in the same thread as the caller?
Please support your answer with a code snippet that conclusively proves your stance.

**Answer**: Yes, Django signals run in the same thread as the caller by default. Since signals are executed synchronously, they will be executed in the same thread that triggers the signal.

#### Example:

```python
from django.dispatch import Signal, receiver
import threading

# Define a custom signal
my_signal = Signal()

# Receiver function to handle the signal
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")

# Function to trigger the signal
def trigger_signal():
    print(f"Trigger function running in thread: {threading.current_thread().name}")
    my_signal.send(sender=None)  # Trigger the signal

# Trigger the signal
trigger_signal()
```

#### Output:

```
Trigger function running in thread: MainThread
Signal handler running in thread: MainThread
```

This demonstrates that the signal runs in the same thread as the caller.

![Question 2 Image](https://github.com/user-attachments/assets/a0d944ae-1a52-4e53-be1b-a998548fafc8)

---

### Question 3: By default, do Django signals run in the same database transaction as the caller?
Please support your answer with a code snippet that conclusively proves your stance.

**Answer**: By default, Django signals do not run in the same database transaction as the caller. Django signals are executed immediately after being sent, regardless of whether the transaction that triggered the signal is committed or rolled back.

#### Example:

```python
from django.db import models
from django.db import transaction
from django.dispatch import Signal, receiver

# Define a test model
class TestModel(models.Model):
    name = models.CharField(max_length=100)

# Define a custom signal
my_signal = Signal()

# Receiver function to handle the signal
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    TestModel.objects.create(name="Created by signal")
    print("Signal handler executed and record created.")

# Function to trigger the signal
def trigger_signal():
    try:
        with transaction.atomic():  # Open a transaction block
            print("Before signal.")
            TestModel.objects.create(name="Created by function")
            my_signal.send(sender=None)  # Trigger the signal
            print("Rolling back transaction.")
            raise Exception("Rolling back the transaction")
    except:
        pass

# Trigger the signal
trigger_signal()
```

#### Output:

```
Before signal.
Signal handler executed and record created.
Rolling back transaction.
```

The signal handler creates a record in the database, even though the transaction is rolled back, proving that it does not run within the same database transaction.

![Question 3 Image](https://github.com/user-attachments/assets/109531eb-d603-4dd2-974b-4c40005c1d60)

---

## Topic: Custom Classes in Python

### Task: Create a Rectangle class with the following requirements:

1. An instance of the `Rectangle` class requires `length: int` and `width: int` to be initialized.
2. We can iterate over an instance of the `Rectangle` class.
3. When iterated, we first get the length in the format: `{'length': <VALUE_OF_LENGTH>}`, followed by the width: `{'width': <VALUE_OF_WIDTH>}`.

#### Solution:

```python
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        # Define an iterator to yield length and width in the specified format
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage
rect = Rectangle(10, 5)

# Iterating over the instance
for dimension in rect:
    print(dimension)
```

#### Output:

```
{'length': 10}
{'width': 5}
```

This code defines a `Rectangle` class that yields the length and width of the rectangle when iterated over.

![Rectangle Class Image](https://github.com/user-attachments/assets/e94e040d-de26-4f9b-a0d1-79afa851222e)

---


```

