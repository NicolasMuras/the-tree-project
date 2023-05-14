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
    
    def create(self, validated_data):
        triangles_data = validated_data.pop('triangles', [])
        id_custom = validated_data.pop('id_custom', 0)
        print(id_custom)
        if id != 0:
            square = Square.objects.create(id=id_custom, **validated_data)
        else:
            square = Square.objects.create(**validated_data)
        triangle_array = []
        for triangle_data in triangles_data:
            coordinates_data = triangle_data.pop('coordinates', [])
            triangle = Triangle.objects.create(square=square, **triangle_data)
            triangle_array.append(triangle)
            coordinate_array = []
            for coordinate_data in coordinates_data:
                coordinate = Coordinate.objects.create(triangle=triangle, **coordinate_data)
                coordinate_array.append(coordinate)
            triangle.coordinates.set(coordinate_array)
        square.triangles.set(triangle_array)
        square.save()
        return square

