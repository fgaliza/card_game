from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from .models import Battle, BattleRound, RoundResult
from .serializers import BattleRoundSerializer, BattleSerializer, RoundResultSerializer
from .utils import calculate_score, save_battle_results, validate_player_cards


class BattleViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Battle.objects.all().order_by('id')
    serializer_class = BattleSerializer


class BattleRoundViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = BattleRound.objects.all()
    serializer_class = BattleRoundSerializer

    def list(self, request, *args, **kwargs):
        battle = Battle.objects.get(id=kwargs['nested_1_pk'])
        battle_rounds = battle.battle_rounds.all()
        serializer = self.get_serializer(battle_rounds, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = BattleRound.objects.get(id=kwargs['pk'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class RoundResultsViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = RoundResult.objects.all()
    serializer_class = RoundResultSerializer

    def list(self, request, *args, **kwargs):
        battle_id = kwargs['nested_1_pk']
        round_number = kwargs['nested_2_pk']

        queryset = RoundResult.objects.filter(
            battle_round__round_number=round_number,
            battle_round__battles__id=battle_id
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        battle_id = kwargs['nested_1_pk']
        round_number = kwargs['nested_2_pk']
        current_round = BattleRound.objects.get(
            battles__id=battle_id,
            round_number=round_number,
        )

        if current_round.results.exists():
            return Response(
                'Round already have results',
                status=status.HTTP_400_BAD_REQUEST,
            )

        results = calculate_score(request.data['results'])
        serializer = RoundResultSerializer(
            data=results,
            many=True,
        )
        serializer.is_valid(raise_exception=True)

        if not validate_player_cards(serializer.validated_data):
            return Response(
                'Invalid card played',
                status=status.HTTP_400_BAD_REQUEST,
            )

        save_battle_results(serializer.validated_data, current_round)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
