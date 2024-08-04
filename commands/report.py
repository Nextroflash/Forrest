import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command()
async def report(ctx, *, bug: str):
    user = ctx.author
    bug_receiver_id = 915483308522086460  # Replace with the receiver's ID

    receiver = await bot.fetch_user(bug_receiver_id)

    embed = discord.Embed(title="Bug Report", color=0xFF0000)
    embed.add_field(name="Reported by", value=user.mention, inline=False)
    embed.add_field(name="Bug Description", value=bug, inline=False)

    await receiver.send(embed=embed)
    await ctx.send("Bug report has been sent successfully!")

def setup(bot):
    bot.add_command(report)