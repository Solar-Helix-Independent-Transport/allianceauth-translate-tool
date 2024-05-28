# AA-Translate-Tool

LibreTranslate Helpers for Alliance Auth.

https://github.com/LibreTranslate/LibreTranslate

## Features

- AA-Discordbot Cog for translation of messages on discord.

## Installation

- Install the app with your venv active

```bash
pip install allianceauth-translate-tool
```

- Add `'aatranslate',` to your INSTALLED_APPS list in local.py.

- Add the below lines to your `local.py` settings file, Changing the contexts to yours.

```python
## Settings for AA-Translate-Tool
# URL of the self hosted libretranslate instance
AA_TRANSLATIONS_URL = "http://URL_to_api:5000"
# Languages we allow in the tool.
AA_TRANSLATIONS_LANGUAGES = []
```
