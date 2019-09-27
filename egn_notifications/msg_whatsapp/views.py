from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import WhatsappSerializer
import itertools
from rest_framework.response import Response
from rest_framework import  status
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
import traceback 
from twilio.rest import Client 
import base64
from django.conf import settings

# Create your views here.


import requests


class WhastappView(APIView):
    """
    Retrieve, update or delete a user instance.
    """    

    def get(self, request,  format=None):
        try:                        
            return Response( "Hola Whatsapp", status=status.HTTP_200_OK)
        except Exception as err:
            print (traceback.format_exc())            
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    
    def send_whats (self, phone, msg) :#, ref, phone):
        #client = Client(settings.ACCOUNT_SID_WHATSAPP, settings.AUTH_TOKEN_WHATSAPP)  
        account_sid = 'AC81cac674583d7fc739fe84d8bfe3dbc1' 
        auth_token = '31cd4c75efd4722a69f23d87e10bc913' 
        client = Client(account_sid, auth_token)         
        message = client.messages.create( 
                                    
                                      from_='whatsapp:+14155238886',  
                                      body='Recibo Electronico Banco Azteca ' + msg,
                                      to='whatsapp:+'  + str (phone)                                    
                                  ) 
         
        print(message.sid)


    def post(self, request,   format=None):
        try:                        
            data_byte = base64.b64decode(request.data['message']['data'])
            data = eval(data_byte.decode("utf-8"))
            serializer = WhatsappSerializer(data=data) 
            if serializer.is_valid():
                self.send_whats (serializer.data['phone'], serializer.data['msg'])
                return Response({},status=status.HTTP_200_OK)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as err:            
            print (traceback.format_exc())
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



