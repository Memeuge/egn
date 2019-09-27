from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import SMSSerializer
import itertools
from rest_framework.response import Response
from rest_framework import  status
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
import traceback 
from twilio.rest import Client 
import base64
from django.conf import settings

# Create your views here.


class SMSView(APIView):
    """
    Retrieve, update or delete a user instance.
    """    

    def get(self, request,  format=None):
        try:                        
            return Response( "Hola SMS", status=status.HTTP_200_OK)
        except Exception as err:
            print (traceback.format_exc())            
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    
    def send_sms (self, phone, msg) :#, ref, phone):
        
        targetURL = "https://api.smsmasivos.com.mx/sms/send"
        # El token se obtienen ejecutando el authSms.py en el cual se envia el API Key para que regrese el token
        # https://app.smsmasivos.com.mx/cuenta
        headers = {
          'token':settings.TOKEN_SMS
        }
        data = {
          'message':msg,
          'numbers':phone,
          'country_code':52
        }
        r = requests.post(url = targetURL, data = data, headers = headers)

        print(r.text)

    def post(self, request,   format=None):
        try:                        
            data_byte = base64.b64decode(request.data['message']['data'])
            data = eval(data_byte.decode("utf-8"))
            serializer = SMSSerializer(data=data) 
            if serializer.is_valid():
                self.send_sms(serializer.data['phone'], serializer.data['msg'])
                return Response({},status=status.HTTP_200_OK)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as err:            
            print (traceback.format_exc())
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

