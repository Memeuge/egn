#django
from django.urls import path
from django.conf.urls import url

from .views import  SMSView

urlpatterns = [        
    url(r'^notif/', SMSView.as_view()),    
    ]