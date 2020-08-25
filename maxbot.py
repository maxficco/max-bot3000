import discord
from discord.ext import commands
from config import *

maxbot = commands.Bot(command_prefix = ["."])

@maxbot.event
async def on_ready():
    print("bot is ready")

@maxbot.event
async def on_member_join(member, ctx):
    print(f"{member} has joined the server! :)")
    await ctx.send(f"Welcome, {member}! Hope you make some friends!")
@maxbot.event
async def on_member_remove(member, ctx):
    print(f"{member} has left the sever. :(")
    await ctx.send(f"{member} left. We hope we can see you later!")
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
