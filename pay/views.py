from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from square.client import Client
import random
import string
client = Client(
        access_token='EAAAEAa7wVPz5T17WOrXMxCLKrzYUk76Rglo9QynVsz7KmA3z-5LxP8bCYlAQTTS',
        environment='sandbox',
    )
payments_api = client.payments
class PaymentView(APIView):

    def get(self,request):
        id = self.request.query_params.get('id',None)
        if id is not None:
            result = payments_api.get_payment(id)
        else:
            result = payments_api.list_payments()
        if result.is_success():
            return Response(result.body, status=status.HTTP_200_OK)
        else:
            return Response(data=result.errors, status=status.HTTP_404_NOT_FOUND)

    def post(self,request, *args, **kwargs):
        body = {}
        body['source_id'] = self.request.data.get("nonce",None)
        body['idempotency_key'] = "".join(random.sample(string.ascii_letters +string.digits, 22))
        body['amount_money'] = {}
        body['amount_money']['amount'] = int(self.request.data.get("amount",None))
        body['amount_money']['currency'] = 'CAD'
        body['autocomplete'] = True
        result = payments_api.create_payment(body)
        if result.is_success():
            return Response(data=result.body, status=status.HTTP_201_CREATED)
        else:
            return Response(data=result.errors, status=status.HTTP_400_BAD_REQUEST)

