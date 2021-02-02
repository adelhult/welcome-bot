from actions.main import *
import schedule
import re
from greet import greet

@add("läsvecka \d+|LV\d+|uppgifter")
async def math(msg):
    """**Läsvecka <n>** - visa uppgifter för vecka n"""
    n = ""
    p = re.compile("läsvecka (\d+)|LV(\d+)|uppgifter vecka (\d+)",
        flags=re.IGNORECASE | re.MULTILINE)
    for match in p.search(msg.content).groups():
        if match is not None:
            n = match
            break

    filename = "./math/week"
    if n == "2":
        filename += "2"
    elif n == "3":
        filename += "3"
    else:
       await msg.channel.send(f"Hittar inga uppgifter för vecka {n}! :(")
       return

    with open(filename + ".txt", 'r', encoding='utf8') as f:
        await msg.channel.send(f.read())


@add("schema|lektion")
async def print_schedule(msg):
    """**Schema** - info om lektioner idag/imorgon/just nu"""
    content = msg.content.lower()

    if "idag" in content or "dagens" in content:
        title, events = schedule.day(0)
        await msg.channel.send(title)
        await send_events(events, msg.channel)
    
    if "imorgon" in content or "morgondag" in content or "i morgon" in content:
        title, events = schedule.day(1)
        await msg.channel.send(title)
        await send_events(events, msg.channel)
    
    if "övermorgon" in content:
        title, events = schedule.day(2)
        await msg.channel.send(title)
        await send_events(events, msg.channel)
        
    if "nästa" in content:
        title, event = schedule.get_next()
        if event is not None:
            await msg.channel.send(title, embed=event)
        else:
             await msg.channel.send(title)
    
    if "nu" in content:
        title, events = schedule.get_current()
        await msg.channel.send(title)
        await send_events(events, msg.channel)

async def send_events(events, channel):
        for event in events:
            await channel.send(embed=event)

@add("härma")
async def imitate(msg):
    """**Härma** - härma det du säger"""
    await msg.channel.send(msg.content)


@add("välkomm(en|na)")
async def welcome(msg):
    """**Välkommen/välkommna** - skicka ett välkomstmeddelande"""
    await msg.channel.send(greet())


@add("källkod")
async def github(msg):
    """**Källkod** - länk till Github repot"""
    await msg.channel.send("Du kan läsa min källkod här! https://github.com/adelhult/welcome-bot/")


@add("hejdå|goodbye|bye|ses sen|hörs")
async def bye(msg):
    """**Hejdå** - Bye bye!"""
    response = choice(["Hejdå!", "Syns sen!", "Bye!", "Hörs"])
    await msg.channel.send(response)


@add("(hej|hi|tja|hallå|tjena|hello)")
async def hello(msg):
    """**Hej** - Hälsa!"""
    await msg.channel.send("hej!")
