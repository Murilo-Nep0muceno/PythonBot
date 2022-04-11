import discord
from discord.ext import commands


# comando que a gente ultiliza para a funcionalidade do bot


bot = commands.Bot("!")


# programa avisa quando esta pronto para o uso

@bot.event
async def on_ready():
    print(f"Estou pronto! estou conectado como {bot.user}")



# comando que detecta quando voce fala algum palavrao


# !oi

@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name

    response = "Olá, você é muito legal " + name

    await ctx.send(response)


@bot.command(name="calcular")
async def calculate(ctx, *expression):
    name = ctx.author.name
    expression = ''.join(expression)
    print(expression)
    responce = eval(expression)

    await ctx.send("a resposta é: vai se fuder,mais facil usar calculadora " + name)
    await ctx.send("toma aqui sua resposta: " + str(responce))




@bot.command(name="odio")
async def segredo(ctx):
     name = ctx.author.name
     await ctx.send("=====Declaração de odio ===== ")
     await ctx.send("Você merece o lixo e não o luxo " + name )
     await ctx.send("nem se você tira seu cerebro e colocar um novo voce fica boa em um jogo " + name)




bot.run("")
