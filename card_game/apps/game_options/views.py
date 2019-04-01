from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from .models import GameOptions
from .serializers import GameOptionsSerializer


class GameOptionsViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = GameOptions.objects.all()
    serializer_class = GameOptionsSerializer

    def list(self, request, *args, **kwargs):
        game_options = GameOptions.objects.last()
        serializer = self.get_serializer(game_options)
        return Response(serializer.data, status.HTTP_200_OK)
