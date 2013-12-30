#!/usr/bin/env python

import signal, sys

from rover.Rover import Rover

def signal_handler(signal, frame):
    print "\n"
    sys.exit(0)

def main():
    rover = Rover()
    print rover.getStatus()

    while True:
        commands = raw_input('Enter commands (fbrl): ')
        try:
            rover.move(commands)
            print rover.getStatus()
        except Exception, e:
            print e

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    main()

