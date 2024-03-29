from colorhash import ColorHash
from discord import Embed, Colour
from requests import get
from ics import Calendar
import arrow


URL = "https://cloud.timeedit.net/chalmers/web/public/ri6Y73QQZ55Zn6Q14854Q8Z85640y.ics"

def get_timeline():
    c = Calendar(get(URL).text)
    return c.timeline

def day(offset):
    """Return the schedule for a given day"""
    date = arrow.utcnow().shift(days=+offset)
    date_str = date.to('local').format('dddd, D MMMM', locale="sv")
    events = list(get_timeline().on(date))
    if len(events) <= 0:
        return (f"Det finns inget planerat för {date_str}!", [])

    msg = f"\n**Schema för {date_str}:**\n"

    return (msg, list(map(gen_event, events)))

def get_current():
    """Get all current events"""
    events = list(get_timeline().now())
    if len(events) <= 0:
        return ("Just nu pågår det ingen händelse!", [])

    return ("Just nu sker detta", list(map(gen_event, events)))

def get_next():
    """Get the next event"""
    t = get_timeline()
    now = arrow.utcnow()
    try:
        event = next(t.start_after(now))
    except StopIteration:
        return ("Det ser inte ut att finnas några kommande händelser", None)

    when = event.begin.humanize(locale="sv")
    return (f"Nästa händelse inträffar {when}", gen_event(event))


def gen_event(event):
    """Generate an embeded item from an event"""
    # Generate start and end dates 
    begin = event.begin.to('local').format("HH:mm")
    end = event.end.to('local').format("HH:mm")
    time = f"Tid: {begin} - {end}"

    title = f"{emoji(event)} **{event.name}**"
    if len(title) > 210:
        title = title[0:200]
    
    desc =  f"{event.description}"

    # generate a color:
    color = Colour.from_rgb(*ColorHash(title).rgb)
    
    # add a location and link if there is one
    location = ""
    if event.location:
        location = f"Plats: {event.location}\n"

    link = ""
    if "TMV170" in event.name:
        link = "https://chalmers.zoom.us/j/65949195103"
    elif "Datakommunikation" in event.name:
        link = "https://chalmers.zoom.us/j/67775432479"

    # create an embeded item
    embed = Embed(title=title,
                  description=location + "\n" + desc,
                  url=link,
                  colour=color)
    
    embed.set_footer(text=time)

    return embed

def emoji(event):
    if "DAT043" in event.name:
        return "<:thinkingAboutJava2:800667732973453312>"
    elif "TMV170" in event.name:
        return "<:anvand_kompendiet:800665026981265438>"
    elif "Maskinorienterad programmering" in event.name:
        return "<:thinkingAboutMOP:823829306563100672>"
    elif "Datatekniskt projekt" in event.name:
        return "<:thinkingAboutMOP:823829306563100672>"
    elif "Datakommunikation" in event.name:
        return "<:HELO:823486677774237707>"
    else:
        return "<:rolf_poggers:794227500464209930>"