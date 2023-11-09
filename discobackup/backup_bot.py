import discord
import time

class BackupBot(discord.Bot):
    class DupeChannel:
        def __init__(self, channel:discord.TextChannel, webhook:discord.Webhook = None):
            self.channel:discord.TextChannel = channel
            self.webhook:discord.Webhook = webhook
    
    # Create a webhook to restore a backup in given text channel
    # Returns either an existing webhook or a newly-created webhook
    async def create_webhook_if_not_exists(self, channel:discord.TextChannel) -> discord.Webhook:
        for hook in await channel.webhooks():
            if hook.user.id == self.user.id:
                return hook
        
        new_hook = await channel.create_webhook(
            name="DiscoBackupHook",
            avatar=await self.user.avatar.read(),
            reason="Restore a text channel"
        )
        
        return new_hook

    # Deletes all webhooks created by this bot from a text channel
    async def delete_webhooks_if_exist(self, channel:discord.TextChannel) -> None:
        for hook in await channel.webhooks():
            if hook.user.id == self.user.id:
                await hook.delete(reason="DiscoBackup no longer needs this hook")
    
    # Creates a new text channel in the same category as the given text channel, with identical permissions
    # Returns the new text channel as an object
    async def duplicate_textchannel(self, channel:discord.TextChannel, new_name:str, add_webhook:bool = False) -> DupeChannel:
        channel = await channel.clone(name=new_name, reason="Created duplicate channel for message restoration")
        webhook = None
        if add_webhook:
            webhook = await self.create_webhook_if_not_exists(channel)
        return self.DupeChannel(channel, webhook)
    
    # Yields messages from present to past
    async def channel_messages(self, channel:discord.TextChannel, min_delay_ms:int):
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
    
    #
    # Callback methods
    #
    
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
            async for iter_message in self.channel_messages(channel, 50):
                if iter_message.author.id != self.user.id:
                    result += "({}) ".format(i)
                    result += iter_message.content
                    result += "\n"
                    i += 1
            if i > 0:
                await message.reply(result)
        if message.content == 'hook':
            await self.create_webhook_if_not_exists(message.channel)
        if message.content == 'delhook':
            await self.delete_webhooks_if_exist(message.channel)
        if message.content.startswith('dupe '):
            await self.duplicate_textchannel(message.channel, message.content[len('dupe '):])
        if message.content.startswith('dupehook '):
            await self.duplicate_textchannel(message.channel, message.content[len('dupehook '):], True)
    