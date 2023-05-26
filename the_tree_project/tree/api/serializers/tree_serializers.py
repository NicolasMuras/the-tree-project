from rest_framework import serializers
from tree.models import Square, Triangle, Coordinate, Trunk


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
    

    
class TrunkSerializer(serializers.ModelSerializer):

    square = SquareSerializer(many=True)

    class Meta:
        model = Trunk
        fields = '__all__'
    
    def get_squares(self, instance):
        return list(instance.squares.values())
    

    def create(self, validated_data):
        squares_data = validated_data.pop('square', [])
        id_custom = validated_data.pop('id_custom', 0)
        """if id_custom != 0:
            trunk = Trunk.objects.create(id=id_custom, **validated_data)
        else:
            trunk = Trunk.objects.create(**validated_data)"""
        trunk = Trunk.objects.create(**validated_data)
        square_array = []
        for square_data in squares_data:
            triangles_data = square_data.pop('triangles', [])
            square= Square.objects.create(trunk= trunk, **square_data)
            square_array.append(square)
            triangle_array = []
            #import pdb; pdb.set_trace()
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
        trunk.square.set(square_array)
        trunk.save()
        return trunk

