import discord
from discord.ext import commands


# comando que a gente ultiliza para a funcionalidade do bot


bot = commands.Bot("!")


# programa avisa quando esta pronto para o uso

@bot.event
async def on_ready():
    print(f"Estou pronto! estou conectado como {bot.user}")






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

    await ctx.send("a resposta é.... Não vou falar " + name)
    await ctx.send(" brincadeira toma aqui sua resposta: " + str(responce))




@bot.command(name="amor")
async def segredo(ctx):
     name = ctx.author.name
     await ctx.send("======Declaração de amor====== ")
     await ctx.send("Você é lindo(a) você merece o mundo " + name )
     await ctx.send("não se preocupe, isso é so uma fase vai passar " + name)




bot.run("")
