#django
from django.urls import path
from django.conf.urls import url

from .views import EmailView

urlpatterns = [    
    url(r'^notif/', EmailView.as_view()),        
    ]