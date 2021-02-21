from discord import Client, Intents, Embed, ChannelType
from greet import greet, get_gif
from actions import act
import sys

try:
    from config import *
except Exception:
    print("You need to create a config object!!")
    sys.exit(1)

class Bot(Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if (self.user in message.mentions
            or message.channel.type == ChannelType.private):
            await act(message)
        
        if (self.user in message.mentions 
            and message.channel.type == ChannelType.private):
            await message.channel.send(
                "Fyi, du behöver inte skriva *@Hacke* när du skickar ett PM till mig!")
    
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            greeting = greet()
            gif = get_gif()
            embed = Embed(title=greeting)
            embed.set_image(url=f"attachment://'welcome.gif")
            await guild.system_channel.send(file=gif, embed=embed)

def main():
    token = conf["token"]

    intents = Intents.default()
    intents.members = True

    client = Bot(intents=intents)
    client.run(token)

    print("The bot is running!")

if __name__ == "__main__":
    main()
