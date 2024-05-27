from django.conf import settings

AA_TRANSLATIONS_LANGUAGES = getattr(
    settings,
    'AA_TRANSLATIONS_LANGUAGES',
    [
        ("English", "en"),
        ("Deutsch", "de"),
        ("Español", "es"),
        ("简体中文", "zh"),
        ("Русский", "ru"),
        ("한국어", "ko"),
        ("Français", "fr"),
        ("日本語", "ja"),
        ("Italiano", "it"),
        ("Українська", "uk")
    ]
)

AA_TRANSLATIONS_URL = getattr(
    settings,
    'AA_TRANSLATIONS_URL',
    "http://libretranslate:9095"
)

AA_TRANSLATIONS_API_KEY = getattr(
    settings,
    'AA_TRANSLATIONS_API_KEY',
    None
)
