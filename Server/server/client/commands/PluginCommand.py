from utils import sendto

from csdata import plugins

from log import logger

class Command:
    aliases = ["plugins","pl"]
    permission = "server.command.plugins"

    def execute(source=None):
        pl = '&f, &a'.join(plugins.lp)
        sendto(source, logger.color(f"&fPlugins ({len(plugins.lp)}): &a{pl}", "&"))

