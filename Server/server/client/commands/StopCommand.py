from utils import sendto

class Command:
    aliases = ["stop"]
    permission = "server.command.stop"

    def execute(source):
        from log import logger
        from csdata import pd
        
        sendto(source, "Stopping server HEHHAHA")
        logger.info("Stopping server", "Command Thread")
        
        pd.path['shutdown']()
