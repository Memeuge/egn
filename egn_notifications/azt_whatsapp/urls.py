#django
from django.urls import path
from django.conf.urls import url

from .views import WhastappView

urlpatterns = [    
    url(r'^notif/', WhastappView.as_view()),    
    ]