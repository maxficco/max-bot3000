import discord
from discord.ext import commands
from config import *
import time
import asyncio
import random

maxbot = commands.Bot(command_prefix = ["."])
maxbot.remove_command("help")

@maxbot.event
async def on_ready():
    print("bot is ready")
    await maxbot.change_presence(activity=discord.Game(name="MaxBot goes Beep Boop"))
@maxbot.event
async def on_member_join(member):
    channel_id = maxbot.get_channel(746945651568410706)
    print(f"{member} joined")
    await member.send(f"Welcome aboard, {member}! Hope you make some friends!")
    await channel_id.send(f"Yay! {member} just joined. Everyone say hi!")
@maxbot.event
async def on_member_remove(member):
    channel_id = maxbot.get_channel(746945651568410706)
    print(f"{member} left")
    await channel_id.send(f"{member} has left the sever 😞")

@maxbot.command()
async def ping(ctx):
    ping = round(maxbot.latency * 1000)
    userping = str(round(maxbot.latency * 1000)) + "ms"
    if ping <50:
        await ctx.send(f"{userping}.  That's Really Good! 🤩")
    elif  50 <= ping < 75:
        await ctx.send(f"{userping}. Pretty Good! 😄")
    elif  75 <= ping < 125:
        await ctx.send(f"{userping}. About Average Speed. 👍")
    elif  125 <= ping < 200:
        await ctx.send(f"{userping}. Your ping is OK, may experience some Lag. 👍")
    elif  ping >= 200:
        await ctx.send(f"{userping}. Lol, your internet sucks. 😂")

@maxbot.command()
async def crystalball(ctx, *, question):
    responses = [
        "It is certain.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

@maxbot.command()
async def hi(ctx):
    await ctx.send(f'Hi there, {str(ctx.author)[:-5]}! I am the Max Bot 3000!\nYou can learn more by typing, ".help"')

@maxbot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@maxbot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@maxbot.command()
async def users(ctx):
    guild_id = maxbot.get_guild(746945651111362662)
    offline = 0
    online = 0
    for user in guild_id.members:
        if user.status == discord.Status.offline:
            offline += 1
        else:
            online += 1
    await ctx.send(f"""```
This server has {guild_id.member_count} Members!
Users Online: {online}
Users Offline: {offline}```""")

@maxbot.command()
async def help(ctx):
    embed = discord.Embed(
        color = discord.Color.orange()
    )
    embed.set_author(name = "Help is on the Way!")
    embed.add_field(name = ".hi", value = "Get a friendly greeting from the Max Bot!")
    embed.add_field(name = ".ping", value = "Returns your Ping in ms!")
    embed.add_field(name = ".users", value = "Lists # of users online & offline!")
    embed.add_field(name = ".crystalball", value = "Just ask a question and it will tell the future!\nex: .crystalball Should I go to Bed?")
    embed.add_field(name = ".kick", value = "Kicks @user out of the server!\nex: .kick @mficco for being rude")
    embed.add_field(name = ".ban", value = "Bans @user from the server!\nex: .ban @mficco for bullying people")
    embed.add_field(name = ".help", value = "shows this page!")
    await ctx.send(embed = embed)

@maxbot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter in all required arguments, following the command.")
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Hey, I can't do that command!")

maxbot.run(api_secret)
