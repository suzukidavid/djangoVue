from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('stock', views.StockView)

urlpatterns = [ 
    path('', include(router.urls)),
    path('get_stock', views.get_stock),
    path('check_stock', views.check_stock)
]