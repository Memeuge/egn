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


    
    def send_whats (self, data):¿ 
        client = Client(settings.ACCOUNT_SID_WHATSAPP, settings.AUTH_TOKEN_WHATSAPP)          
        message = client.messages.create( 
                                    #media_url=['https://ibero.mx/campus/publicaciones/contabilidad/pdf/recibodinero.pdf'],
                                    #media_url=['http://saitenlinea.com/manualv2/images/thumb/2/2a/ReciboNomina02.jpg/700px-ReciboNomina02.jpg'],
                                    #media_url=['https://uploads-ssl.webflow.com/575ef60509a5a7a9116d9f8c/58a8aaa1cd722ae171dde008_imageedit_60_5318139676.png'],
                                    #media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'],
                                      from_='whatsapp:+14155238886',  
                                      body='PRUEBA WHATSAPP DESDE PYTHON de la API',      
                                      to='whatsapp:+5217771063311' 
                                       #to='whatsapp:+5215512875816' 
                                       #to='whatsapp:+5215554078439' 
                                  ) 
         
        print(message.sid)


    def post(self, request,   format=None):
        try:                        
            data_byte = base64.b64decode(request.data['message']['data'])
            data = eval(data_byte.decode("utf-8"))
            serializer = WhatsappSerializer(data=data) 
            if serializer.is_valid():
                self.send_whats (serializer.data)
                return Response({},status=status.HTTP_200_OK)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as err:            
            print (traceback.format_exc())
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

