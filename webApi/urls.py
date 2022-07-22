from django.urls import include, path
from rest_framework import routers

from webApi.controllers import RegisterAPI
from webApi.controllers.categoria.categoria_viewset import CategoriaViewSet
from webApi.controllers.detalleVenta.detalleVenta_viewset import DetalleVentaViewSet
from webApi.controllers.producto.producto_viewset import ProductoViewSet
from webApi.controllers.stock.stock_viewset import StockViewSet
from webApi.controllers.venta.venta_viewset import VentaViewSet

router = routers.DefaultRouter()
router.register(r'ventas', VentaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'detalleVentas', DetalleVentaViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'stocks', StockViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPI.as_view(), name='register'),
]