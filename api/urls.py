from django.urls import include, path
from rest_framework import routers
from api.products.views import ProductViewSet
from api.clients.views import ClientGenericViewSet
from api.order.views import OrderViewSet


router = routers.DefaultRouter()

router.register(r'products', ProductViewSet)

router.register(r'clients', ClientGenericViewSet)

router.register(r'order', OrderViewSet)


urlpatterns = [
    path('api/', include(router.urls))
]