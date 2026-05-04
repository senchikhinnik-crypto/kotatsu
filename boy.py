import discord
from discord.ext import commands
import os
import random
from threading import Thread
from flask import Flask

# ====== ВЕБ-СЕРВЕР ДЛЯ RENDER ======
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Бот работает!"

def run_web():
    app.run(host='0.0.0.0', port=10000)

Thread(target=run_web, daemon=True).start()
# ====================================

# ====== ДАННЫЕ БОТА ======
TOKEN = os.getenv("TOKEN")
ID_KANALA_PRIVETSTVIE = 1500808393655455754  # ID канала приветствия

# ====== НАСТРОЙКИ БОТА ======
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
            title=f"⚔️ Врата открылись, {member.name}!",
            description=selected_phrase,
            color=0x2C2F33
        )
        embed.set_image(url="https://iili.io/BQuojfe.png")
        
        await channel.send(embed=embed)

# ====== ЗАПУСК ======
@bot.event
async def on_ready():
    print(f"✅ Бот {bot.user} запущен!")

bot.run(TOKEN)