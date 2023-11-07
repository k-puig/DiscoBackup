import argparse
import sys

import discord

import discobackup
from discobackup.backup_bot import BackupBot

parser = argparse.ArgumentParser(
    description='A Discord bot to backup and restore text channels, messages, and all attached media.'
)
parser.add_argument('-v', '--version', action='version', version='discobackup ' + discobackup.__version__)
parser.add_argument('filename')

def main(argv=None) -> int:
    if argv is None:
        argv = sys.argv
    
    args = parser.parse_args(argv[1:])
    
    # Show discord library version
    print("Using " + discord.__title__ + " version " + discord.__version__)
    
    # Define intents
    intents = discord.Intents.default()
    intents.message_content = True
    
    # Get token as string
    token_filename = args.filename
    with open(token_filename, 'r') as f:
        token = f.read()
    
    # Start bot
    bot = BackupBot(intents=intents)
    bot.run(token)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())