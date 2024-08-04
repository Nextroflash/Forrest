import discord
from discord.ext import commands
from keep_alive import keep_alive
import datetime
from discord.ext.commands import has_permissions
import os
TOKEN = os.environ['TOKEN']

intents = discord.Intents.all()
intents.messages = True
intents.guilds = True
intents.members = True
intents.guild_messages = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print("\033[92m[+] All commands valid.")
    print("[+] Bot Token Received.")
    print("[+] Bot Logged in.")
    print("[+] Bot Ready to Respond to commands.")

@bot.command()
async def report(ctx, *, bug: str):
    bug_receiver_id = 915483308522086460
    receiver = await bot.fetch_user(bug_receiver_id)

    embed = discord.Embed(title="Bug Report", color=0xFF0000)
    embed.add_field(name="Reported by", value=ctx.author.mention, inline=False)
    embed.add_field(name="Bug Description", value=bug, inline=False)

    await receiver.send(embed=embed)
    await ctx.send("Bug report has been sent successfully!")

@bot.command()
async def commands(ctx):
    command_list = [
        "**Commands List**",
        "`.limit <limit>` - Sets the user limit for a voice channel",
        "`.report <bug>` - Report bugs",
        "`.commands` - Displays available commands",
        "`.uptime` - Displays how long the bot has been online for",
        "`.cmds` - Displays all available commands",
        "`.cc <name>` - Creates a channel ",
        "`.cd <name/id>` - Deletes a channel",
    ]

    embed = discord.Embed(
        title='Commands List',
        description='\n'.join(command_list),
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)
  
@bot.command()
async def limit(ctx, limit: int):
    try:
        voice_channel = ctx.author.voice.channel
        await voice_channel.edit(user_limit=limit)
        embed = discord.Embed(
            title="User Limit Update",
            description=f"The user limit for {voice_channel.name} has been set to {limit}.",
            color=discord.Color.dark_blue()
        )
        await ctx.send(embed=embed)
    except AttributeError:
        embed = discord.Embed(
            title="User Limit Update",
            description="Please join a voice channel to use this command.",
            color=discord.Color.dark_blue()
        )
        await ctx.send(embed=embed)

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel is not None and after.channel != before.channel:
        if after.channel.name == "Join To Create":
            new_channel = await after.channel.category.create_voice_channel(f"{member.display_name}'s vc")
            await new_channel.edit(user_limit=2)
            await member.move_to(new_channel)

    if before.channel:
        if len(before.channel.members) == 0 and before.channel.name.endswith("'s vc"):
            await before.channel.delete()

start_time = datetime.datetime.now()

@bot.command()
async def uptime(ctx):
    current_time = datetime.datetime.now()
    uptime = current_time - start_time

    days = uptime.days
    hours, remainder = divmod(uptime.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    embed = discord.Embed(title="Bot Uptime", color=discord.Color.blue())
    embed.add_field(name="Days", value=f"{days}")
    embed.add_field(name="Hours", value=f"{hours}")
    embed.add_field(name="Minutes", value=f"{minutes}")
    embed.add_field(name="Seconds", value=f"{seconds}")

    await ctx.send(embed=embed)

@bot.command()
@has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel = None):
    if channel is None:
        channel = ctx.channel

    # Ensure only users with the "Administrator" permission can talk
    for role in ctx.guild.roles:
        if role.permissions.administrator:
            await channel.set_permissions(role, send_messages=True)
        else:
            await channel.set_permissions(role, send_messages=False)

    await ctx.send(f"{channel.mention} has been locked. Only Administrators can talk.")

@bot.command()
@has_permissions(manage_channels=True)
async def hide(ctx, channel: discord.TextChannel = None):
    if channel is None:
        channel = ctx.channel

    await channel.set_permissions(ctx.guild.default_role, read_messages=False)
    await ctx.send(f"{channel.mention} has been hidden.")

@bot.command()
@has_permissions(manage_channels=True)
async def lockall(ctx):
    for channel in ctx.guild.channels:
        await channel.set_permissions(ctx.guild.default_role, send_messages=False)

    await ctx.send("All channels have been locked.")

@bot.command()
@has_permissions(manage_channels=True)
async def hideall(ctx):
    for channel in ctx.guild.channels:
        await channel.set_permissions(ctx.guild.default_role, read_messages=False)

    await ctx.send("All channels have been hidden.")

@bot.command()
@has_permissions(manage_channels=True)
async def unlock(ctx, channel: discord.TextChannel = None):
    if channel is None:
        channel = ctx.channel

    # Set send_messages permission to True for all roles in the channel
    for role in ctx.guild.roles:
        await channel.set_permissions(role, send_messages=True)

    await ctx.send(f"{channel.mention} has been unlocked. All roles can talk.")

@bot.command()
@has_permissions(manage_channels=True)
async def unhide(ctx, channel: discord.TextChannel = None):
    if channel is None:
        channel = ctx.channel

    # Set read_messages permission to True for all roles in the channel
    for role in ctx.guild.roles:
        await channel.set_permissions(role, read_messages=True)

    await ctx.send(f"{channel.mention} has been unhidden. All roles can read messages.")

@bot.command()
async def cmds(ctx):
    command_list = [
        "**Commands List**",
        "`/limit <limit>` - Sets the user limit for a voice channel",
        "`/report <bug>` - Report bugs",
        "`/commands` - Displays available commands",
        "`/uptime` - Displays how long the bot has been online for",
        "`/ban <user>` - Bans member",
        "`/kick <user>` - Kicks member",
        "`/addrole <user> <role>` - Adds a role to any member",
        "`/avatar <user>` - Shows any member's avatar",
        "`/warn <user>` - Warns member",
        "`/clearwarnings <user>` - Clears a member's warnings",
        "`/deafen <user>` - Deafens a member",
        "`/giveaway <details>` - Host a giveaway",
        "`/invite` - Gives an invite link to the server",
        "`/meme` - Sends a meme",
        "`/move <user> <channel>` - Moves a member to a different voice channel",
        "`/mute <user>` - Mutes member",
        "`/ping` - Check if the bot is online",
        "`/purge <amount>` - Clears messages in bulk",
        "`/reactionrole-setup` - Setup reaction roles",
        "`/removerole <user> <role>` - Removes a role from a member",
        "`/removetimeout <user>` - Removes timeout from a member",
        "`/report <user> <reason>` - Report a user",
        "`/skin <player>` - Shows any Minecraft player's skin",
        "`/slowmode <time>` - Sets slowmode for a channel",
        "`/softban <user>` - Soft bans a user",
        "`/timeout <user> <duration>` - Timeout a member",
        "`/unban <user>` - Unbans a member",
        "`/unmute <user>` - Unmutes a member",
        "`/undeafen <user>` - Undeafens a member",
        "`/vmute <user>` - Mutes member in voice channel",
        "`/vkick <user>` - Kicks a member from a voice channel",
        "`/warn <user> <reason>` - Warn a member",
        "`/warnings <user>` - Show warnings of a user"
    ]

    embed = discord.Embed(
        title='Commands List',
        description='\n'.join(command_list),
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def membercount(ctx):
    embed = discord.Embed(title=f"Member Count: {ctx.guild.name}", description=f"Total Members: {ctx.guild.member_count}", color=discord.Color.blue())
    await ctx.send(embed=embed)

@bot.command()
async def cc(ctx, name):
    guild = ctx.guild
    await guild.create_text_channel(name)

    embed = discord.Embed(
        title="Channel Created",
        description=f"The channel '{name}' has been created successfully.",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
async def cd(ctx, identifier):
    guild = ctx.guild
    try:
        channel_id = int(identifier)
        channel = discord.utils.get(guild.channels, id=channel_id)
    except ValueError:
        channel = discord.utils.get(guild.channels, name=identifier)

    if not channel:
        embed = discord.Embed(
            title="Error",
            description=f"Channel '{identifier}' not found.",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)
        return

    await channel.delete()

    embed = discord.Embed(
        title="Channel Deleted",
        description=f"The channel '{channel.name}' has been deleted successfully.",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

keep_alive()
bot.run(TOKEN)