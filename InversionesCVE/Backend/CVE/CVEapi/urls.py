from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("Personal", views.PersonalViewSet)
router.register("Cliente", views.clienteViewSet)
router.register("Facturas", views.facturasViewSet)
router.register("Usuarios", views.usuariosViewSet)
router.register("Contratos", views.contratosViewSet)



urlpatterns = router.urls