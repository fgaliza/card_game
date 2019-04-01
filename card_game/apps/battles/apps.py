from django.apps import AppConfig


class BattlesConfig(AppConfig):
    name = 'apps.battles'

    def ready(self):
        from apps.battles import signals  # noqa
