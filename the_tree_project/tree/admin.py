from django.contrib import admin

# Register your models here.
from tree.models import Square, Triangle, Coordinate, Trunk

class CoordinateAdmin(admin.ModelAdmin):
    list_display = ('id', 'x', 'y',)

class TriangleAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_coordinates',)

class SquareAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_triangles',)

class TrunkAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_squares')

admin.site.register(Coordinate, CoordinateAdmin)
admin.site.register(Triangle, TriangleAdmin)
admin.site.register(Square, SquareAdmin)
admin.site.register(Trunk, TrunkAdmin)
