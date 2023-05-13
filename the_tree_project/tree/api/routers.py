from rest_framework.routers import DefaultRouter
from tree.api.views.tree_viewsets import SquareViewSet


router = DefaultRouter()
router.register(r'', SquareViewSet, basename='Square')

urlpatterns = router.urls
