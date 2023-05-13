from rest_framework import serializers
from tree.models import Square


class SquareSerializer(serializers.ModelSerializer):

    class Meta:
        model = Square
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'triangles': instance.triangles
        }
