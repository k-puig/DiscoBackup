import argparse
import sys

import discobackup

parser = argparse.ArgumentParser(
    description='A Discord bot to backup and restore text channels, messages, and all attached media.'
)
parser.add_argument('-v', '--version', action='version', version='discobackup ' + discobackup.__version__)

def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    parser.parse_args(argv[1:])
    
    print("Hello world!")
    
    return 0