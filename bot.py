import discord
from discord.ext import commands
import os
import random

# ====== ДАННЫЕ БОТА ======
TOKEN = os.getenv("TOKEN")  # Токен в Render, НЕ в коде!
ID_KANALA_PRIVETSTVIE = 1500808393655455754  # ID канала приветствия (ПРОВЕРЬ!)

# ====== НАСТРОЙКИ ======
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ====== ПРИВЕТСТВИЕ ======
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(ID_KANALA_PRIVETSTVIE)
    if channel:
        phrases = [
            "«Если боль не убьет тебя, она сделает тебя сильнее»",
            "«Восстань, мой верный воин»",
            "«Твоя тень всегда будет следовать за тобой»",
            "«Даже самый слабый может стать легендой»",
            "«Смерть не остановит того, кто поклялся в верности»"
        ]
        selected_phrase = random.choice(phrases)
        
        embed = discord.Embed(
            title=f"⚔️ Врата открылись, {member.mention}!",
            description=selected_phrase,
            color=0x2C2F33
        )
        embed.set_image(url="https://iili.io/BQuojfe.png")  # Твоя картинка
        
        await channel.send(embed=embed)

# ====== ЗАПУСК ======
@bot.event
async def on_ready():
    print(f"✅ Бот {bot.user} запущен!")

bot.run(TOKEN)