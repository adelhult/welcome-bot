import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

def main():
    client = MyClient()
    client.run('TOKEN')

if __name__ == '__main__':
    main()