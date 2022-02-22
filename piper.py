#!/usr/bin/python3
"""
Hope you enjoy the code
"""
import time
import argparse
import util
import logging, logging.config
from datetime import datetime
import json, yaml

logging.config.fileConfig('config/logger.conf', defaults={'logfilename': f'logs/server.log-{datetime.now().strftime("%Y%m%d%H%M%S")}.log'})
logger = logging.getLogger('consoleLogger')

config = None
with open('config/default.yml') as fs:
    try:
        config = yaml.safe_load(fs)
    except yaml.YAMLError:
        raise 'Failed to load project settings yaml file.'

help_msg='''
        --create-payload     - Create a client payload.
        --connect            - Connects to a running server
        --daemon             - Runs the server in the background
    -h, --host               - Host url/ip
    -p, --port               - Host port which the server runs

Examples:
    Creating a payload:
    \tpython3 piper.py --create-payload --host myawesomehost.com --port 9696
    \t\tpython3 piper.py -c -h myawesomehost.com -p 9696
    
    Running server as daemon:
    \tpython3 piper.py --daemon
    \tpython3 piper.py --daemon --host 0.0.0.0 --port 5555

    Connect to running server:
    \tpython3 piper.py --connect  --host 0.0.0.0 --port 5555
    \tpython3 piper.py 
'''

parser = argparse.ArgumentParser(add_help=False, usage=help_msg)
parser.add_argument('--create-payload', action="store_true", dest="create_payload", help="Create a client payload")
parser.add_argument('--daemon', action="store_true", help="Runs the server in the background")
parser.add_argument('--connect', action="store_true", help="Connects to a running server")
parser.add_argument('--host', '-h', type=str, dest="host", help="Host of the server")
parser.add_argument('--port', '-p', type=str, dest="port", help="Port of the server")

args = parser.parse_args()

def main():
    util.clear_screen()
    logger.info(util.get_banner())
    #load settings
    host = config['server']['host'] if args.host is None else args.host
    port = config['server']['port'] if args.port is None else args.port
    
    if args.create_payload:
        logger.info(f"Creating payload pointing to {host}:{port}")
    else:
        logger.info(f"Starting server on {host}:{port}")
        #TODO
        if args.daemon:
            logger.info("Starting server on background")
        else:
            logger.info("Running server")

if __name__ == "__main__":
    main()