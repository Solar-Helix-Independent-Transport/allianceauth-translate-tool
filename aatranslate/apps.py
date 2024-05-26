from django.apps import AppConfig

from . import __version__


class AATranslateConfig(AppConfig):
    name = 'aatranslate'
    label = 'aatranslate'
    verbose_name = f'Translation Tool v{__version__}'
