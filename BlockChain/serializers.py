from rest_framework import serializers
from .models import BlockChain

class BlockChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockChain
        fields = '__all__'

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request', None)
        if request and request.method == 'POST':
            fields.pop('status', None)
        return fields
