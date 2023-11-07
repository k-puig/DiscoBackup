import discord
import time

class BackupBot(discord.Bot):
    # Yields messages from present to past
    async def channel_messages_iterable(self, channel:discord.TextChannel, min_delay_ms:int):
        if not (type(min_delay_ms) is int):
            print("min_delay_ms is " + str(type(min_delay_ms)))
            yield ()
            return
        
        if not (type(channel) is discord.TextChannel):
            print("channel is " + str(type(channel)))
            yield ()
            return

        time1 = time.time() * 1000
        async for message in channel.history(limit=None):
            time2 = time.time() * 1000
            
            time_elapsed = time2 - time1
            if time_elapsed < min_delay_ms and min_delay_ms - time_elapsed > 0:
                time.sleep((min_delay_ms - time_elapsed) / 1000)
            
            yield message
            
            time1 = time.time() * 1000
    
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    
    async def on_message(self, message):
        if message.content == 'hello':
            await message.reply('world!')
        if message.content == 'iterate':
            result = ""
            channel = message.channel
            
            # minimum ms delay between iterations is set to 50 ms in case of rate limits
            # adjust as needed as development continues
            i = 0
            async for iter_message in self.channel_messages_iterable(channel, 50):
                if iter_message.author.id != self.user.id:
                    result += "({}) ".format(i)
                    result += iter_message.content
                    result += "\n"
                    i += 1
            await message.reply(result)
    