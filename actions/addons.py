from discord import File, Embed
from requests import get
from greet import greet
from actions.main import *
from config import *
import schedule
from random import choice
import re
import io


@add("`.*`")
async def plot(msg):
    """**Rita graf** Skriv exempelvis `x^2` så plottar jag det!"""
    api = conf["plot_api"]

    # find the provided function:
    p = re.compile("`(?:.*=)?(.*)`",
        flags=re.IGNORECASE | re.MULTILINE)
    fn = p.search(msg.content).groups()[0].strip()
    
    # get potential extra params from the user
    y_min = get_param("y_min", msg.content, -10)
    y_max = get_param("y_max", msg.content,  10)
    x_min = get_param("x_min", msg.content, -10)
    x_max = get_param("x_max", msg.content,  10)

    # get the filename of the videos
    filename = get(
        api + "/generate/",
        timeout=20,
        params={
            "fn": fn,
            "y_min": y_min,
            "y_max": y_max,
            "x_min": x_min,
            "x_max": x_max
        },).text
    
    # error?
    if filename == "":
        await msg.channel.send("Attans! Jag kunde inte tolka det!")
        return

    # send the video file to the channel
    file_data = get(f"{api}/videos/{filename}", timeout=20).content
    f = File(io.BytesIO(file_data), filename=filename)
    await msg.channel.send(file=f)

def get_param(name, src, fallback):
    """Get param like name=<int>, else return the fallback"""
    p = re.compile(rf"{name}\s*=\s*(-?\d+)",
        re.IGNORECASE | re.MULTILINE)
    try:
        result = p.search(src).groups(1)[0].strip()
        return int(result)
    except Exception:
        return fallback

@add("läsvecka \d+|LV\d+|uppgifter vecka \d+")
async def math(msg):
    """**Läsvecka <n>** - Visa uppgifter för vecka n """
    
    n = None
    p = re.compile("läsvecka (\d+)|LV(\d+)|uppgifter vecka (\d+)",
        flags=re.IGNORECASE | re.MULTILINE)
    
    for number in p.search(msg.content).groups():
        if number is not None:
            n = int(number)
            break

    filename = f"./math/week{number}.txt"
    
    # cancel if they did not enter a number (should not really happen)
    if number is None:
        await msg.channel.send(f"Förstår inte vad du menar! :(")
        return
    
    try:
        # I think that this should be somewhat safe, since I only allow
        # the end user to input an integer
        with open(filename, 'r', encoding='utf8') as f:
            await msg.channel.send(f.read())
    except Exception:
        await msg.channel.send(f"Hittar inga uppgifter för vecka {n}! :(")

@add("schema|lektion")
async def print_schedule(msg):
    """**Schema** - info om lektioner idag/imorgon/just nu """
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

@add("boka|grupprum")
async def booking(msg):
    """**Boka grupprum** - skicka länken för att boka ett grupprum"""
    link = "https://cloud.timeedit.net/chalmers/web/b1/"
    await msg.channel.send(f"Här är länken för att boka ett grupprum på campus:\n {link}")

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

# should aways be of lowest priority 
@add(lambda _: True)
async def failure(msg):
    # otherwise... print a failure phrase
    await msg.channel.send(choice(failure_phrase))

failure_phrase = [
    "Jag förstår inte vad du menar :(",
    "Jag vet inte hur man gör det tyvärr <:rolf_poggers:794227500464209930>",
    "Kan du förklara igen? Jag förstod inte <:denhar_smorjan:800665072653172747>",
    "Jag förstår inte <:anvand_kompendiet:800665026981265438>",
    "Jag förstår inte hur man gör det (än...)"
]
