from rest_framework import routers

from .views import GameOptionsViewSet

app_name = "game-options"

router = routers.DefaultRouter()
router.register(r'game-options', GameOptionsViewSet, basename='game-options')

urlpatterns = []
urlpatterns += router.urls
