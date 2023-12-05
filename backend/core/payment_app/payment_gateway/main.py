import razorpay
from django.conf import settings


class RazorPayClient:

          def __init__(self)->None:
                    try:
                              self._client = razorpay.Client(auth=(
                                                  settings.RAZORPAY_KEY_ID,
                                                  settings.RAZORPAY_KEY_SECRET
                                                  )
                                        )
                    except Exception as e:
                              print(e)

          def create_order(self,amount:int,currency:str)->dict:
                    try:
                              _data = {
                                        "amount": amount*100,
                                        "currency": currency,
                              }
                              return self._client.order.create(data=_data)
                    except Exception as e:
                            raise Exception(str(e))
          def verify_payment_signature(self,razorpay_order_id:str, razorpay_payment_id:str, razorpay_signature:str)->bool:
                  try:
                              return self._client.utility.verify_payment_signature({
                                                  'razorpay_order_id': razorpay_order_id,
                                                  'razorpay_payment_id': razorpay_payment_id,
                                                  'razorpay_signature': razorpay_signature
                                                  })
                  except Exception as e:
                          raise Exception(str(e))