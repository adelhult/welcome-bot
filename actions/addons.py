from actions.main import *
import analys
from greet import greet

@add("läsvecka 2")
async def week2(msg):
    """**Läsvecka 2** - visa läsvecka 2 """
    await msg.channel.send(analys.week2())


@add("schema")
async def schedule(msg):
    """**Schema** - länk till schemat"""
    await msg.channel.send("Här är vårt schema:\nhttps://cloud.timeedit.net/chalmers/web/public/ri1Y93ygZ05ZZQQ1X75v5Y075Q45x4966g080YQQ617.html")


@add("härma")
async def imitate(msg):
    """**Härma** - härma det du säger"""
    await msg.channel.send(msg.content)


@add("välkomm")
async def welcome(msg):
    """**Välkommen/välkommna** - skicka ett välkomstmeddelande"""
    await msg.channel.send(greet())


@add("källkod")
async def github(msg):
    """**Källkod** - länk till Github repot"""
    await msg.channel.send("Du kan läsa min källkod här! https://github.com/adelhult/welcome-bot/")


@add("hejdå")
async def bye(msg):
    """**Hejdå** - Bye bye!"""
    response = choice(["Hejdå!", "Syns sen!", "Bye!", "Hörs"])
    await msg.channel.send(response)


@add("hej")
async def hello(msg):
    """**Hej** - Hälsa!"""
    await msg.channel.send("hej!")
