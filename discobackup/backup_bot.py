import discord

class BackupBot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    
    async def on_message(self, message):
        if message.content == 'hello':
            await message.reply('world!')
    