from libretranslatepy import LibreTranslateAPI

from .app_settings import AA_TRANSLATIONS_API_KEY, AA_TRANSLATIONS_URL


class LibreTranslateClient:
    def __init__(self):
        if AA_TRANSLATIONS_API_KEY:
            self.t = LibreTranslateAPI(
                AA_TRANSLATIONS_URL,
                api_key=AA_TRANSLATIONS_API_KEY
            )
        else:
            self.t = LibreTranslateAPI(
                AA_TRANSLATIONS_URL
            )

    def translate(self, text, source="auto", target="en"):
        output = self.t.translate(text, source, target)
        return output

    def languages(self):
        output = self.t.languages()
        return output


translate = LibreTranslateClient()
