from django.urls import include, path
from rest_framework import routers
from api.products import views


router = routers.DefaultRouter()

router.register(r'products', views.ProductViewSet)


urlpatterns = [
    path('api/', include(router.urls))
]