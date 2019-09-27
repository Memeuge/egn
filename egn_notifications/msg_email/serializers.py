from rest_framework import serializers

class EmailSerializer(serializers.Serializer):        
    #type_notif = serializers.ListField(required=True)    
    #type_transaction = serializers.CharField(required=True)    
    #folio_transaction = serializers.CharField(required=True)        
    email = serializers.EmailField(required=True)
    msg = serializers.CharField(required=True)
    #monto = serializers.IntegerField(required=True)

    