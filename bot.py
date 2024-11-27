import discord
from discord.ext import commands
from token import TOKEN  # Importa o token do bot

# Configurações do bot
intents = discord.Intents.default()
intents.members = True  # Permite ao bot ver eventos relacionados a membros, como quando alguém entra ou sai
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento que acontece quando o bot está pronto
@bot.event
async def on_ready():
    print(f'Bot está pronto! Logado como {bot.user}')

# Evento que acontece quando um novo membro entra no servidor
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='geral')  # Canal 'geral' como exemplo
    if channel:
        await channel.send(f'Bem-vindo ao servidor, {member.mention}! 🎉')

# Comando de boas-vindas
@bot.command()
async def regras(ctx):
    await ctx.send("1. Seja respeitoso.\n2. Não faça spam.\n3. Siga as regras do servidor.")

# Comando para banir usuário
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} foi banido(a) do servidor. Motivo: {reason}')

# Comando para expulsar usuário
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} foi expulso(a) do servidor. Motivo: {reason}')

# Comando para limpar mensagens
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'{amount} mensagens foram deletadas!', delete_after=5)

# Comando de ajuda (opcional)
@bot.command()
async def help(ctx):
    help_text = """
    **Comandos disponíveis:**
    - !ban [usuário] [motivo] - Bane um usuário.
    - !kick [usuário] [motivo] - Expulsa um usuário.
    - !clear [número] - Limpa as últimas [número] mensagens.
    - !regras - Mostra as regras do servidor.
    """
    await ctx.send(help_text)

# Inicia o bot
bot.run(TOKEN)
