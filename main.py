from discord import Client, Intents, Embed, ChannelType
from greet import greet, get_gif
from actions import act

class Bot(Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if (self.user in message.mentions
            or message.channel.type == ChannelType.private):
            await act(message)
    
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            greeting = greet()
            gif = get_gif()
            embed = Embed(title=greeting)
            embed.set_image(url=f"attachment://'welcome.gif")
            await guild.system_channel.send(file=gif, embed=embed)

def main():
    with open('token.txt', 'r') as f:
        token = f.read().strip()

    intents = Intents.default()
    intents.members = True

    client = Bot(intents=intents)
    client.run(token)

    print("The bot is running!")

if __name__ == "__main__":
    main()
