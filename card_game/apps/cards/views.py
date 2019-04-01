from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Card
from .serializers import CardDetailSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all().order_by('-power')
    serializer_class = CardDetailSerializer

    def retrieve(self, request, pk):
        try:
            try:
                card = Card.objects.get(id=int(pk))
            except ValueError:
                card = Card.objects.get(name=pk)
        except ObjectDoesNotExist as ex:
            msg = ex.args[0]
            return Response(msg, status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(card)
        return Response(serializer.data, status.HTTP_200_OK)
