from random import choice
import re

failure_phrase = [
    "Jag förstår inte vad du menar :(",
    "Jag vet inte hur man gör det tyvärr <:rolf_poggers:794227500464209930>",
    "Kan du förklara igen? Jag förstod inte <:denhar_smorjan:800665072653172747>",
    "Jag förstår inte <:anvand_kompendiet:800665026981265438>",
    "Jag förstår inte hur man gör det (än...)"
]

actions = []

def add(predicate):
    """
    A decorator used to register a new action
    ```
    @add("hej")
    def hello(msg):
        return "hello"
    ```
    """

    # If the predicate is a string,
    # treat it as a regex and convert it to a lambda
    # expression
    if type(predicate) is str:
        regex = re.compile(predicate, flags=re.IGNORECASE | re.MULTILINE)
        p = lambda s: regex.search(s) is not None

    def decorator(func):
        actions.append((p, func))
        return func
    
    return decorator

def description():
    """Generate a description of all the actions"""
    summery = []
    for _, func in actions:
        if func.__doc__:
           summery.append(__doc__)

    return "Här är några av de saker jag kan göra:\n" + "\n".join(summery)



async def act(msg):
    """Parse the msg and try to act upon a users request"""

    if "hjälp" in msg.content.lower():
        await msg.channel.send(description())
    
    for matches, action in actions:
        if matches(msg.content):
            await action(msg)
            break

    # otherwise... print a failure phrase
    choice(failure_phrase)
