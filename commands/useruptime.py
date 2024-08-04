from discord.ext import commands
import datetime

bot = commands.Bot(command_prefix='.')

@bot.command()
async def useruptime(ctx):
    uptime = datetime.datetime.now() - ctx.author.created_at
    hours, remainder = divmod(uptime.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    uptime_str = f"{int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"
    await ctx.send(f"User Uptime: {uptime_str}")

def setup(bot):
    bot.add_command(useruptime)
