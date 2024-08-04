from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.command()
async def limit(ctx, limit: int):
    voice_channel = ctx.message.author.voice.channel
    if voice_channel:
        await voice_channel.edit(user_limit=limit)
        await ctx.send(f"The user limit for {voice_channel.name} has been set to {limit}.")
    else:
        await ctx.send("You are not in a voice channel.")

def setup(bot):
    bot.add_command(limit)
