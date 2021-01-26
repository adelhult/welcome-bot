from actions.add import *
from greet import greet

@add("test")
async def test(msg):
    print(msg.content)
    await msg.channel.send("hej!!!!!!")

@add("schema")
async def schedule(msg):
    await msg.channel.send("Här är vårt schema:\nhttps://cloud.timeedit.net/chalmers/web/public/ri1Y93ygZ05ZZQQ1X75v5Y075Q45x4966g080YQQ617.html")

@add("härma")
async def imitate(msg):
    await msg.channel.send(msg.content)

@add("välkomm")
async def welcome(msg):
    await msg.channel.send(greet())

@add("källkod")
async def github(msg):
    await msg.channel.send("Du kan läsa min källkod här! https://github.com/adelhult/welcome-bot/")

@add("hejdå")
async def bye(msg):
    response = choice(["Hejdå!", "Syns sen!", "Bye!", "Hörs"])
    await msg.channel.send(response)

@add("hej")
async def bye(msg):
    await msg.channel.send("hej!")