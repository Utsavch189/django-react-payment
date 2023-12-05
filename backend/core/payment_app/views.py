from typing import Any
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from payment_app.payment_gateway.main import RazorPayClient
from .models import Transaction
from django.utils import timezone
import uuid

class PaymentOrderController(APIView):

          def __init__(self, **kwargs: Any) -> None:
                  self._rz=RazorPayClient()
          
          def post(self,request)->Response:
                    try:
                          _resp=self._rz.create_order(
                                  amount=request.data['amount'],
                                  currency=request.data['currency']
                          )
                          return Response({"message":"order_id created","data":_resp},status=status.HTTP_201_CREATED)
                    except Exception as e:
                              return Response({"message":e},status=status.HTTP_400_BAD_REQUEST) 

class PaymentVerifyController(APIView):
        
          def __init__(self, **kwargs: Any) -> None:
                self._rz=RazorPayClient()
          
          def post(self,request)->Response:
                    try:
                          _resp=self._rz.verify_payment_signature(
                                  razorpay_order_id=request.data['razorpay_order_id'],
                                  razorpay_payment_id=request.data['razorpay_payment_id'],
                                  razorpay_signature=request.data['razorpay_signature']
                          )
                          _transaction_id=uuid.uuid1()
                          _tx=Transaction(
                              transaction_id=_transaction_id,
                              razorpay_order_id=request.data['razorpay_order_id'],
                              razorpay_payment_id=request.data['razorpay_payment_id'],
                              razorpay_signature=request.data['razorpay_signature'],
                              amount=request.data['amount'],
                              datetime=timezone.now()
                          )
                          _tx.save()
                          return Response({"message":"payment verfied","verify_status":_resp,"transaction_id":_transaction_id},status=status.HTTP_200_OK)
                    except Exception as e:
                              return Response({"message":e},status=status.HTTP_400_BAD_REQUEST)
          
