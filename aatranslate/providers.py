from libretranslatepy import LibreTranslateAPI
from openai import OpenAI

from .app_settings import (
    AA_TRANSLATIONS_API_KEY,
    AA_TRANSLATIONS_PROVIDER,
    AA_TRANSLATIONS_MODEL,
    AA_TRANSLATIONS_URL,
)


class LibreTranslateClient:
    def __init__(self):
        if AA_TRANSLATIONS_API_KEY:
            self.t = LibreTranslateAPI(
                AA_TRANSLATIONS_URL, api_key=AA_TRANSLATIONS_API_KEY
            )
        else:
            self.t = LibreTranslateAPI(AA_TRANSLATIONS_URL)

    def translate(self, text, source="auto", target="en"):
        output = self.t.translate(text, source, target)
        return output

    def languages(self):
        output = self.t.languages()
        return output


class OpenAITranslateClient:
    def __init__(self):
        self.client = OpenAI(
            base_url=AA_TRANSLATIONS_URL, api_key=AA_TRANSLATIONS_API_KEY
        )

    def translate(self, text, source="auto", target="en"):
        completion = self.client.chat.completions.create(
            extra_headers={},
            extra_body={},
            temperature=0,
            model=AA_TRANSLATIONS_MODEL,
            messages=[
                {
                    "role": "developer",
                    "content": f"You are a translator. Translate strictly from {source} to {target}. Output only the translated text in full with no additions.",
                },
                {
                    "role": "user",
                    "content": text,
                },
            ],
        )
        return completion.choices[0].message.content.strip()

    def languages(self):
        return []


translate = None
if AA_TRANSLATIONS_PROVIDER == "libretranslate":
    translate = LibreTranslateClient()
elif AA_TRANSLATIONS_PROVIDER == "openai":
    translate = OpenAITranslateClient()
else:
    raise Exception("Unknown translate provider")
