from discord import Client, Intents
from greet import greet, getGif
from actions import act

class Bot(Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if self.user not in message.mentions:
            return 
        answer = act(message.content)
        await message.channel.send(answer)   
        await message.channel.send(getGif())
    
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            await guild.system_channel.send(greet())

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
