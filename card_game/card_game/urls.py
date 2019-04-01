from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.cards.routes')),
    path('', include('apps.players.routes')),
    path('', include('apps.game_options.routes')),
    path('', include('apps.battles.routes')),
    path('docs/', include_docs_urls(title='CardGame API')),
]
