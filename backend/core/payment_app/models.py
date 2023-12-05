from django.db import models
from django.utils import timezone
from datetime import datetime

class Transaction(models.Model):
          transaction_id=models.CharField(max_length=100,primary_key=True,default="")
          razorpay_order_id=models.CharField(max_length=100,null=True,blank=True)
          razorpay_payment_id=models.CharField(max_length=100,null=True,blank=True)
          razorpay_signature=models.CharField(max_length=100,null=True,blank=True)
          amount=models.CharField(max_length=10,null=True,blank=True)
          datetime=models.DateTimeField(default=datetime.now())

          def __str__(self) -> str:
                  return self.transaction_id