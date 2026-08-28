from rest_framework.routers import DefaultRouter
from .views import UserViewSet, NetworkConnectionViewSet
router=DefaultRouter(); router.register('users',UserViewSet); router.register('connections',NetworkConnectionViewSet, basename='connection')
urlpatterns=router.urls
