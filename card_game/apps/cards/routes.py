from rest_framework import routers

from .views import CardViewSet

app_name = "cards"

router = routers.DefaultRouter()
router.register(r'cards', CardViewSet, basename='cards')

urlpatterns = []
urlpatterns += router.urls
