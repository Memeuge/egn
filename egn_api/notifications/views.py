from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import NotificationsSerializer
import itertools
from rest_framework.response import Response
from rest_framework import  status
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
import traceback 
from twilio.rest import Client 
import base64
from django.conf import settings
from google.cloud import pubsub_v1


# Create your views here.


class NotificationsView(APIView):
    """
    Retrieve, update or delete a user instance.
    """    

    def get(self, request,  format=None):
        try:                        
            return Response( "Hola Notifications", status=status.HTTP_200_OK)
        except Exception as err:
            print (traceback.format_exc())            
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def enqueue_data (self, phone, email, msg, type_msg):
        project_id = settings.PROJECT_ID_QUEUE
        #message = "Mensaje...."
        
        if  "WHATSAPP" in type_msg:
            topic_name = settings.TOPIC_NAME_QUEUE_WHATSAPP
        if  "EMAIL" in type_msg :
            topic_name = settings.TOPIC_NAME_QUEUE_EMAIL
        if  "SMS" in type_msg :
            topic_name = settings.TOPIC_NAME_QUEUE_EMAIL

        publisher = pubsub_v1.PublisherClient()
        # The `topic_path` method creates a fully qualified identifier
        # in the form `projects/{project_id}/topics/{topic_name}`
        topic_path = publisher.topic_path(project_id, topic_name)


        #for n in range(1, 2):
            #data = message + u'Message number {}'.format(n)

        data = {
                'phone': phone,
                'email':email,
                'msg': msg
                }
        data = str (data).encode()
        print (data)
        
        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data=data)
        print(future.result())

        print('Published messages.')

    
    def post(self, request,   format=None):
        try:                                    
            serializer = NotificationsSerializer(data=request.data) 
            if serializer.is_valid():
                self.enqueue_data (serializer.data['phone'], serializer.data['email'], serializer.data['msg'], serializer.data['type_notif'] )
                return Response({},status=status.HTTP_200_OK)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as err:            
            print (traceback.format_exc())
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

