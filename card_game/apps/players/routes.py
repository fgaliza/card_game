from rest_framework import routers

from .views import PlayerViewSet

app_name = "players"

router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet, basename='players')

urlpatterns = []
urlpatterns += router.urls
