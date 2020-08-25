import discord
from discord.ext import commands
from config import *
import time
import asyncio

maxbot = commands.Bot(command_prefix = ["."])

@maxbot.event
async def on_ready():
    print("bot is ready")

@maxbot.event
async def on_member_join(member):
    channel = maxbot.get_channel(746945651568410706)
    print(f"{member} joined")
    casual = member[:-4]
    await member.send(f"Welcome aboard, {casual}! Hope you make some friends!")
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

maxbot.run(api_secret)
