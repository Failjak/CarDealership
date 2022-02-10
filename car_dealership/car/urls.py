from rest_framework import routers

from .views import CarViewSet, CarPricesViewSet, CarConfigViewSet

router = routers.SimpleRouter()
router.register(r'car', CarViewSet, basename='car')
router.register(r'car_price', CarPricesViewSet, basename='car_price')
router.register(r'car_config', CarConfigViewSet, basename='car_configuration')

urlpatterns = router.urls
