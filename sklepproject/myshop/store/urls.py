from rest_framework import routers
from .views import RatesViewSet,ClothingViewSet
from django.urls import include,path
router=routers.DefaultRouter()
router.register(r'clothing',ClothingViewSet)
router.register(r'rates', RatesViewSet)

urlpatterns=[
    path('api/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework'))
]