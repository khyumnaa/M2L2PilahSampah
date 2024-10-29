import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def animals(ctx):
    img_name = random.choice(os.listdir('animals'))  
    with open(f'animals/{img_name}', 'rb') as f:  
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

sampah_organik = ["daun", "buah busuk", "kotoran hewan", "ampas teh", "sisa sayuran"]
sampah_anorganik = ["plastik", "kaca", "logam", "keramik", "detergen"]
sampah_b3 = ['baterai bekas', 'minyak bekas', 'sisa obat-obatan', 'pertisida', 'oli bekas']

@bot.command()
async def pilih(ctx):
    while True:
        await ctx.send('Masukkan sampah:')
        msg = await bot.wait_for('message')
        if msg.content in sampah_organik:
            await ctx.send('Masukkan dalam organik')
        elif msg.content in sampah_anorganik:
            await ctx.send('Masukkan dalam anorganik')
        elif msg.content in sampah_b3:
            await ctx.send('Masukkan dalam B3')
        else: #kondisi ketika entri yang di input tidak ada maka program berhenti
            await ctx.send('Maaf entri tidak ada, maka program berhenti')
            break
bot.run('enter your token here')
