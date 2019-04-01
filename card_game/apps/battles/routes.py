from rest_framework_nested import routers

from apps.battles.views import BattleRoundViewSet, BattleViewSet, RoundResultsViewSet
from apps.players.views import PlayerHandViewSet

app_name = "battles"

router = routers.DefaultRouter()
router.register(r'battles', BattleViewSet, basename='battles')

battle_rounds_router = routers.NestedDefaultRouter(router, r'battles')
battle_rounds_router.register(r'rounds', BattleRoundViewSet)

round_results_router = routers.NestedDefaultRouter(
    battle_rounds_router,
    r'rounds',
)
round_results_router.register(r'round_results', RoundResultsViewSet)

player_hand_router = routers.NestedDefaultRouter(router, r'battles')
player_hand_router.register(r'players', PlayerHandViewSet)


urlpatterns = []
urlpatterns += router.urls
urlpatterns += battle_rounds_router.urls
urlpatterns += round_results_router.urls
urlpatterns += player_hand_router.urls
