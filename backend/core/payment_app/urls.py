from django.urls import path
from .views import PaymentOrderController,PaymentVerifyController

urlpatterns = [
    path('order/',PaymentOrderController.as_view(),name='payment-order'),
    path('verify/',PaymentVerifyController.as_view(),name='payment-verify')
]
