from rest_framework import routers

from .views import DealerViewSet

router = routers.SimpleRouter()
router.register(r'dealer', DealerViewSet, basename='dealer')

urlpatterns = router.urls
