import discord
from discord import app_commands
from discord.ext import commands
import os
import random
TOKEN = "Use o Token Aqui!"  

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online como {bot.user}!")
    try:
        synced = await bot.tree.sync()
        print(f"Comandos sincronizados: {len(synced)}")
    except Exception as e:
        print(e)


@bot.tree.command(name="emoji", description="Envia um emoji")
async def emoji_cmd(interaction: discord.Interaction):
    await interaction.response.send_message("🔥")


@bot.tree.command(name="gif", description="Envia um GIF")
async def gif_cmd(interaction: discord.Interaction):
    await interaction.response.send_message(
        "https://media.tenor.com/7xT2ZVjMxEAAAAAC/mario-dance.gif"
    )


@bot.tree.command(name="membros", description="Mostra quantos membros tem no servidor")
async def membros_cmd(interaction: discord.Interaction):
    membros = interaction.guild.member_count
    await interaction.response.send_message(
        f"👥 Este servidor tem **{membros} membros**."
    )


@bot.tree.command(name="meuid", description="Mostra o ID do usuário que usou o comando")
async def meuid_cmd(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"🆔 Seu ID é: **{interaction.user.id}**"
    )

@bot.command()
async def meme(ctx):
    images = os.listdir("images")
    aleatorios = random.choice(images)
    with open(f"images/{aleatorios}", 'rb') as meme:
        image = discord.File(meme , filename="image.png")
        embed = discord.Embed(title="meme", color=discord.Color.blue())
        embed.set_image(url="attachment://image.png")
        await ctx.send(embed=embed , file=image)

@bot.command()
async def youtube(ctx): 
    youtubers = [
        "https://www.youtube.com/@a.d.i.s.s.a.u.r.o",
        "https://www.youtube.com/@FamiRex"


    ]
    await ctx.send(random.choice(youtubers))
bot.run(Use o Token Aqui!")
