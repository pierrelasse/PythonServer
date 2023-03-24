from log import logger
from csdata import cd
from utils import sendto, getusername

class Command:
    aliases = ["list"]
    permission = "server.command.list"

    def execute(source):
        connected = cd.clients_connected

        size = len(connected)
        list = ', '.join([getusername(c) for c in connected])
        text = f"There are currently {size} client{'' if size == 1 else 's'} connected: {list}"
        
        sendto(source, logger.color(text, "&"))
