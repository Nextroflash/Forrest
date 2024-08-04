from discord.ext import commands
import datetime

bot = commands.Bot(command_prefix='.')

@bot.command()
async def botuptime(ctx):
    now = datetime.datetime.now()
    created_at = bot.user.created_at.replace(tzinfo=datetime.timezone.utc)
    uptime = now - created_at
    await ctx.send(f"The bot has been online for {uptime}")

def setup(bot):
    bot.add_command(botuptime)
