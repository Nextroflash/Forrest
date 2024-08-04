from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='.')

@bot.command()
async def commandlist(ctx):
    command_list = [
        "**Commands List**",
        "`.limit <limit>` - Sets the user limit for a voice channel",
        "`.report <bug>` - Report bugs",
        "`.commandlist` - Displays available commands"
    ]

    embed = discord.Embed(
        title='Commands List',
        description='\n'.join(command_list),
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)

def setup(bot):
    bot.add_command(commandlist)
