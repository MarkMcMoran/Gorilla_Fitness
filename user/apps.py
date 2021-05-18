from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'user'

    def ready(self):
        import user.signals
