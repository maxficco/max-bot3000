import discord
from discord.ext import commands
from config import *
import time
import asyncio
import random

maxbot = commands.Bot(command_prefix = ["."])

@maxbot.event
async def on_ready():
    print("bot is ready")
    await maxbot.change_presence(activity=discord.Game(name="MaxBot goes Beep Boop"))
@maxbot.event
async def on_member_join(member):
    channel = maxbot.get_channel(746945651568410706)
    print(f"{member} joined")
    await member.send(f"Welcome aboard, {member}! Hope you make some friends!")
    await channel.send(f"Yay! {member} just joined. Everyone say hi!")
@maxbot.event
async def on_member_remove(member):
    channel = maxbot.get_channel(746945651568410706)
    print(f"{member} left")
    await channel.send(f"{member} has left the sever 😞")
@maxbot.command()
async def checkmyping(ctx):
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
    await ctx.send(f'Hi There! I am the Max Bot 3000! I hope you are doing well.\nYou can find out more by typing, ".help"')
@maxbot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
@maxbot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)


@maxbot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter in all required arguments, following the command.")

maxbot.run(api_secret)
