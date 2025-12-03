import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True   

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def joined(ctx, member: discord.Member):
    "Mostra quando o usuario entrou no servidor"
    await ctx.send(f'{member.name} entrou no servidor em {member.joined_at.strftime("%d/%m/%Y %H:%M")}')
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="geral")
    if channel:
        await channel.send(f"👋 Bem-vindo ao servidor, {member.mention}!")

bot.run("SEU_TOKEN_AQUI")
