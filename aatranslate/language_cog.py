# Cog Stuff
import logging

import discord
from discord import Message, ui
from discord.ext import commands

# AA Contexts
from django.conf import settings
from .providers import translate as t
from .app_settings import AA_TRANSLATIONS_LANGUAGES
logger = logging.getLogger(__name__)


# def get_languages():
#     languages = t.languages()
#     out = []
#     for _l in languages[:24]:
#         out.append(
#             discord.SelectOption(
#                 label=_l["name"],
#                 value=_l["code"]
#             )
#         )
#     return out


def get_languages():
    languages = AA_TRANSLATIONS_LANGUAGES
    out = []
    for _l in languages[:24]:
        out.append(
            discord.SelectOption(
                label=_l[0],
                value=_l[1]
            )
        )
    return out


class LanguageDropdown(discord.ui.Select):
    """
        Language Select Dropdown for discord message to summon a translation.
    """

    def __init__(self, message):
        super().__init__(
            placeholder="Language",
            options=get_languages(),
        )
        self.message = message

    async def callback(self, interaction: discord.Interaction):
        translated = t.translate(self.message, target=self.values[0])
        await interaction.response.edit_message(
            content=(
                f"{translated} "
            ),
            view=None,
        )


class LanguageView(ui.View):
    """
        View for picking a group to assign a help thread too
    """

    def __init__(self, message):
        super().__init__(LanguageDropdown(message))


class LanguageCog(commands.Cog):
    """
        Language Cog Things
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.message_command(name="Translate")
    async def translate(self, interaction, message: Message):
        msg = await interaction.response.send_message(
            "Please Wait...",
            ephemeral=True
        )
        await msg.edit(
            content="Choose Language",
            view=LanguageView(message.content)
        )


def setup(bot):
    bot.add_cog(LanguageCog(bot))
