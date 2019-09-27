from rest_framework import serializers

class WhatsappSerializer(serializers.Serializer):        
    #type_notif = serializers.ListField(required=True)    
    #type_transaction = serializers.CharField(required=True)    
    #folio_transaction = serializers.CharField(required=True)        
    phone = serializers.IntegerField(required=True)
    msg = serializers.CharField(required=True)
    #monto = serializers.IntegerField(required=True)

    