import argparse
import sys

import discord

import discobackup
from discobackup.backup_bot import BackupBot

parser = argparse.ArgumentParser(
    description='A Discord bot to backup and restore text channels, messages, and all attached media.'
)
parser.add_argument('-v', '--version', action='version', version='discobackup ' + discobackup.__version__)

def token_as_string() -> str:
    with open("bot_token.txt") as token:
        token_str = token.read()
    
    return token_str

def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    parser.parse_args(argv[1:])
    
    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = BackupBot(intents=intents)
    bot.run(token_as_string())
    
    return 0