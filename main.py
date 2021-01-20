import discord

class WelcomeBot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

def main():
    with open('token.txt', 'r') as f:
        token = f.read().strip()

    client = WelcomeBot()
    client.run(token)

if __name__ == '__main__':
    main()