from rest_framework import mixins, viewsets

from .models import Player
from .serializers import PlayerHandSerializer, PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('-name')
    serializer_class = PlayerSerializer


class PlayerHandViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerHandSerializer
