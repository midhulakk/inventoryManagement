from invent_app.models import Item
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields='__all__'
        read_only=['id','added_on']

    def __str__(self):
        return self.name
