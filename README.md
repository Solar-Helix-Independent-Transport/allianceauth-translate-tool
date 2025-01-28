# AA-Translate-Tool

LibreTranslate Helpers for Alliance Auth.

https://github.com/LibreTranslate/LibreTranslate

## Features

- AA-Discordbot Cog for translation of messages on discord.

## Installation

- Install and setup LibreTranslate from its docs, configure as required.

- Install the app with your venv active or add it to your requirements.txt for Docker

```bash
pip install allianceauth-translate-tool
```
or 
```
allianceauth-translate-tool==version
```

- Add `'aatranslate',` to your INSTALLED_APPS list in local.py.

- Add the below lines to your `local.py` settings file, Changing the contexts to yours.

```python
## Settings for AA-Translate-Tool
# URL of the self hosted libretranslate instance
AA_TRANSLATIONS_URL = "http://URL_to_api:5000"
# Optional Api Key
AA_TRANSLATIONS_API_KEY= "i was generated from libretranslate"
# Languages we allow in the tool. list of ("Display Name", "language code https://libretranslate.com/languages") or leave as is for defaults
# AA_TRANSLATIONS_LANGUAGES = []
```

## Usage

![discord context menu showing app usage](docs/app_usage.png)

![bot response to clicking the app in the context menu](docs/message.png)

![bot response ](docs/translated.png)

## Libretranslate System Requirements

Seems to be CPU bound using around 2gb of memory. On a 2 core, 4gb instance it takes around a minute to translate 60 words. 
