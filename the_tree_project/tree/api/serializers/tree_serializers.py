from rest_framework import serializers
from tree.models import Square, Triangle, Coordinate


class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'x': instance.x,
            'y': instance.y
        }

class TriangleSerializer(serializers.ModelSerializer):
    coordinates = CoordinateSerializer(many=True)

    class Meta:
        model = Triangle
        fields = '__all__'

class SquareSerializer(serializers.ModelSerializer):

    triangles = TriangleSerializer(many=True)

    class Meta:
        model = Square
        fields = '__all__'

    def get_triangles(self, instance):
        return list(instance.triangles.values())

