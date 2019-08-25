from rest_framework import serializers

class WhatsappSerializer(serializers.Serializer):    
    #email = serializers.EmailField(required=True)
    phone = serializers.IntegerField(required=True)
    msg = serializers.CharField(required=True)    
    