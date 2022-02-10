from rest_framework import routers

from .views import OfferViewSet, DiscountViewSet

router = routers.SimpleRouter()
router.register(r'offer', OfferViewSet, basename='offer')
router.register(r'discount', DiscountViewSet, basename='discount')

urlpatterns = router.urls
