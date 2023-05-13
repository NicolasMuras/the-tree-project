from django.db import models


class Coordinate(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()

class Triangle(models.Model):
    coordinates = models.ManyToManyField(Coordinate)

    def get_coordinates(self):
        return "\n".join([str(c) for c in self.coordinates.all()])

class Square(models.Model):
    triangles = models.ManyToManyField(Triangle)

    def get_triangles(self):
        return "\n".join([str(t) for t in self.triangles.all()])