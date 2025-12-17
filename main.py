import discord
from discord import app_commands
from discord.ext import commands
import os
import random
TOKEN = "Use seu Token Aqui!"  

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
async def reciclar(ctx):
    reciclar = [
        "1. Lixeira Azul: Papel (jornais, revistas, folhas)",
        "2. Lixeira Vermelha: Plástico (garrafas, sacolas, embalagens)",
        "3. Lixeira Verde: Vidro (garrafas, potes, frascos)",
        "4. Lixeira Amarela: Metal (latas, tampas, alumínio)",
        "5. Lixeira Marrom: Orgânico (restos de comida, cascas, folhas)",
        "6. Lixeira Cinza: Rejeitos (fraldas, papel higiênico, lixo sujo)"
    ]
    recilar = "\n".join(reciclar)
    await ctx.send((reciclar))

@bot.command()
async def ajudar(ctx):
    ajudar = [
        "Para ajudar o planeta com menos gases poluentes você pode", 
        "1. Usar transporte público ou bicicleta", 
        "2. Reduzir o consumo de energia elétrica", 
        "3. Se possivel troque as lãmpadas incandescentes ou fluorescentes por LED",
        "4. Compartilhe com outras pessoas essas informações",
    ]
    ajudar = "\n".join(ajudar)
    await ctx.send((ajudar))


@bot.command()
async def perigo(ctx):
    perigo = [
      "Os perigos do aquecimento global incluem:", 
       "1. Aumento do nível do mar, ameaçando comunidades costeiras", 
       "2. Eventos climáticos extremos, como furacões e secas", 
       "3. Perda de biodiversidade e habitats naturais", 
       "4. Impactos na agricultura e segurança alimentar",
    ]
    perigo = "\n".join(perigo)
    await ctx.send((perigo))


bot.run("Use seu Token Aqui!!")
