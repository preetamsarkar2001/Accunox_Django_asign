# signal_demo/urls.py
from django.contrib import admin
from django.urls import path
from question1 import views
from question2 import views as question2_views
from question3 import views as question3_views
from rectangle_app import views as rectangle_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('trigger-signal/', views.trigger_signal_view, name='trigger_signal'),
    path('trigger-thread-signal/', question2_views.trigger_signal_for_thread_test, name='trigger_thread_signal'),
    path('test-transaction-signal/', question3_views.test_signal_transaction_view, name='test_transaction_signal'),
     path('rectangle/', rectangle_views.rectangle_view, name='rectangle_view'),
]
