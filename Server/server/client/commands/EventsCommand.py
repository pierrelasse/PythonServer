from utils import sendto

from log import logger

from csdata import plugins

class Command:
    aliases = ["events"]
    permission = "server.command.events"

    def execute(source):
        sendto(source, logger.color("&<E92280>Listing events please wait...", "&"))
        logger.warn(plugins.revents)
        for event in plugins.revents:
            sendto(source, logger.color(f"&<0009B6>EVENT &<0C0C0F>> &<0ED588>{event}", "&"))
        sendto(source, logger.color("&<30E922>Events listed!", "&"))