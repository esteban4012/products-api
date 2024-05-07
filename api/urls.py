from django.urls import include, path
from rest_framework import routers
from api.products.views import ProductViewSet
from api.clients.views import ClientGenericViewSet


router = routers.DefaultRouter()

router.register(r'products', ProductViewSet)

router.register(r'clients', ClientGenericViewSet)


urlpatterns = [
    path('api/', include(router.urls))
]