from rest_framework.routers import DefaultRouter
from tree.api.views.tree_viewsets import TrunkViewSet


router = DefaultRouter()
router.register(r'', TrunkViewSet, basename='Trunk')

urlpatterns = router.urls
