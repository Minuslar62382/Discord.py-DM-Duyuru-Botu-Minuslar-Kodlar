import discord
from discord.ext import commands

# Genişletilmiş intents ayarları
intents = discord.Intents.default()
intents.message_content = True  # Mesaj içeriğine erişim sağlar
intents.members = True  # Sunucudaki tüm üyelere erişim sağlar

# Kullanıcıdan Token'ı al
TOKEN = input("Bot Token'ınızı girin: ")

# Prefix'i belirleyin
bot = commands.Bot(command_prefix='!!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} olarak giriş yapıldı.')

@bot.command(name='duyur')
@commands.has_permissions(administrator=True)
async def duyur(ctx, *, duyuru_metni):
    await ctx.send(f"Duyuru gönderiliyor: {duyuru_metni}")
    sayac = 0
    for member in ctx.guild.members:
        if member.bot:
            continue
        try:
            await member.send(duyuru_metni)
            sayac += 1
        except discord.Forbidden:
            print(f"{member} kullanıcısına mesaj gönderilemedi.")
    await ctx.send(f"Duyuru {sayac} kişiye gönderildi.")

@duyur.error
async def duyur_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bu komutu kullanmak için yetkiniz yok.")

bot.run(TOKEN)