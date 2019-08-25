#django
from django.urls import path
from django.conf.urls import url

from .views import WhastappView, SMSView

urlpatterns = [    
    url(r'^notif/', WhastappView.as_view()),    
    url(r'^sms/', SMSView.as_view()),    
    ]