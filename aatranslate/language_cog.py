# Cog Stuff
import logging

import discord
from discord import Message, ui
from discord.ext import commands

from .app_settings import AA_TRANSLATIONS_LANGUAGES
from .providers import translate as t


logger = logging.getLogger(__name__)


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
        await interaction.response.defer()
        translated = t.translate(self.message, target=self.values[0])
        await interaction.edit(
            content=(
                f"{translated} "
            ),
            view=None,
        )


class LanguageView(ui.View):
    """
        View for picking a the language
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
