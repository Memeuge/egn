from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import EmailSerializer
import itertools
from rest_framework.response import Response
from rest_framework import  status
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
import traceback 
from twilio.rest import Client 
import base64
from django.conf import settings

# Create your views here.


class EmailView(APIView):
    """
    Retrieve, update or delete a user instance.
    """    

    def get(self, request,  format=None):
        try:                        
            return Response( "Hola Email", status=status.HTTP_200_OK)
        except Exception as err:
            print (traceback.format_exc())            
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    
    def send_mail (email, msg):  
        themsg = MIMEMultipart()
        themsg['Subject'] = 'Resultados de Riesgos financieros'
        themsg['To'] = email #", ".join(to_addr)
        themsg['From'] = settings.FROM_ADDR
        html = '''
            <html>
                <head></head>
                <body>
                    
                    <br>
                    <h3>Recibo Electronico Banco Azteca: </h3>
                    <br>
                    <p>
                    
                        Detalle: %s
                    </p>
                    
                    <p>
                        Gracias!!.
                    </p>
                    
                </body>
            </html>
        ''' % (msg)

        part1 = MIMEText(html, 'html', 'utf-8')
        themsg.attach(part1)    
        server = smtplib.SMTP(settings.MAIL_SERVER)
        server.ehlo()
        server.starttls()
        server.login(settings.USERNAME_EMAIL,settings.EMAIL_PASS)
        server.sendmail(settings.FROM_ADDR, email, str(themsg))
        server.quit()

        print ('Email ok')


    def post(self, request,   format=None):
        try:                        
            data_byte = base64.b64decode(request.data['message']['data'])
            data = eval(data_byte.decode("utf-8"))
            serializer = EmailSerializer(data=data) 
            if serializer.is_valid():
                self.send_mail (serializer.data['email'], serializer.data['msg'])
                return Response({},status=status.HTTP_200_OK)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as err:            
            print (traceback.format_exc())
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

