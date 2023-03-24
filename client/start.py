import os
import sys

from client.Client import Main

def start():
    Main(sys.argv)


if os.name == "nt":
    start()