from rest_framework import routers

from .views import ProviderViewSet

router = routers.SimpleRouter()
router.register(r'provider', ProviderViewSet, basename='provider')

urlpatterns = router.urls
