from re import findall

import discord
from discord.ext.commands import Context, group

from utils import Cog


class Fun(Cog):
    """A cog for fun commands"""

    @group(invoke_without_command=True)
    async def how_many(self, ctx: Context, *, text):
        """Shows the amount of people that has the supplied text in their display name."""
        text = text.strip().lower()
        if text == "asked":
            return await ctx.send("Nobody.")
        await ctx.send(
            f"{sum((text in member.display_name.lower()) for member in ctx.guild.members)} people have `{text}` (any case) in their display name."
        )

    @how_many.command()
    async def regex(self, ctx: Context, *, regex):
        """Shows the amount of people that has the supplied regex in their display name."""
        await ctx.send(
            f"{sum(bool(findall(regex, x.display_name)) for x in ctx.guild.members)} people have `{regex}` in their display name."
        )

    @group(invoke_without_command=True)
    async def poll(self, ctx: Context, question, choice1, choice2):
        """Create a poll."""
        message = await ctx.send(
            embed=discord.Embed(
                title=f"Poll | {question}",
                description=f":a: {choice1}\n:b: {choice2}",
                color=discord.Color.brand_red(),
            ).set_author(
                name=ctx.author.display_name, icon_url=ctx.author.display_avatar
            )
        )
        await message.add_reaction("🅰")
        await message.add_reaction("🅱")

    @poll.command()
    async def yesno(self, ctx: Context, *, question):
        """Create a poll with the options being yes or no."""
        message = await ctx.send(
            embed=discord.Embed(
                title="Yes/No Poll",
                description=question,
                color=discord.Color.brand_green(),
            ).set_author(
                name=ctx.author.display_name, icon_url=ctx.author.display_avatar
            )
        )
        await message.add_reaction("✅")
        await message.add_reaction("❎")


def setup(bot):
    bot.add_cog(Fun(bot))
