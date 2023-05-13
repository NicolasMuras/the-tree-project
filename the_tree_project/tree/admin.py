from django.contrib import admin

# Register your models here.
from tree.models import Square, Triangle, Coordinate

class CoordinateAdmin(admin.ModelAdmin):
    list_display = ('id', 'x', 'y',)

class TriangleAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_coordinates',)

class SquareAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_triangles',)

admin.site.register(Coordinate, CoordinateAdmin)
admin.site.register(Triangle, TriangleAdmin)
admin.site.register(Square, SquareAdmin)