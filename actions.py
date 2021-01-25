from random import choice
from greet import greet
import analys
import re

class Action():
    def __init__(self, predicate, action):
        self.predicate = predicate
        self.action = action

    def fulfill(self, msg):
        if type(self.action) is str:
            return self.action
        # ...otherwise
        return self.action(msg)        
        
    def matches(self, msg):
        # if the predicate is a string,
        # treat it as a regex. 
        if type(self.predicate) is str:
            return re.search(self.predicate, msg,
                flags=re.IGNORECASE | re.MULTILINE) is not None
        
        # ...otherwise treat the predicate 
        # as an actual function
        return self.predicate(msg)

def act(msg):
    for action in actions:
        if action.matches(msg):
            return action.fulfill(msg)

    # if we could not find 
    # a matching action, return an error
    return choice(failure_phrase)

# if you want add more behaviors to the bot
# just add another Action to the list!
actions = [
    Action(
        "schema",
        "Här är vårt schema:\nhttps://cloud.timeedit.net/chalmers/web/public/ri1Y93ygZ05ZZQQ1X75v5Y075Q45x4966g080YQQ617.html"
    ),
    Action(
        "läsvecka 2",
        analys.week2()
    ),
    Action(
        "härma",
        lambda msg: msg
    ),
    Action(
        "välkomm",
        lambda _: greet() 
    ),
    Action(
        "källkod",
        "Du kan läsa min källkod här! https://github.com/adelhult/welcome-bot/"
    ),
    Action("hejdå",
        "Syns sen!"
    ),
    Action(
        "hej",
        "**Hej på dig!** :)"
    ),
    Action(
        "tack",
        "Ingen fara <:tackArr:794227156347387966>!"
    )
]

failure_phrase = [
    "Jag förstår inte vad du menar :(",
    "Jag vet inte hur man gör det tyvärr <:rolf_poggers:794227500464209930>",
    "Kan du förklara igen? Jag förstod inte <:denhar_smorjan:800665072653172747>",
    "Jag förstår inte <:anvand_kompendiet:800665026981265438>",
    "Jag förstår inte hur man gör det (än...)"
]
    
