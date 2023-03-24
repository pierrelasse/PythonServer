from utils import sendto

from csdata import plugins

from log import logger

from csdata import commands

class Command:
    aliases = ["reload"]
    permission = "server.command.reload"

    def execute(source=None):
        sendto(source, logger.color(f"&cRELOADING...", "&"))
        commands.load()
        sendto(source, logger.color(f"&aReloaded! Reloaded &2{len(commands.cmds)} &acommands.", "&"))

