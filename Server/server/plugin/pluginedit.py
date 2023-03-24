from csdata import plugins

class logger:
    def info(message):
        _log.info(f"{message}", "Plugin-%plugin_name%", "&")
    
    def error(message):
        _log.error(f"{message}", "Plugin-%plugin_name%", "&")
        
    def warn(message):
        _log.warn(f"{message}", "Plugin-%plugin_name%", "&")

class plugin:
    sendto = _sendto
    
    def registerEvent(func, type):
        logger.warn("The event system is currently disabled due to your mom being fat aka python doing PROBGLEMS >:(", "Plugin-%plugin_name%")

        type = str(type)
        types = ['OnJoin','OnQuit','OnCommand','OnChat']

        if not type in types:
            logger.error(f"Error while registering event! Unknown type. [Type: '{type}' Func: '{func.__name__}']")
            return

        plugins.revents.append({
            "event": type,
            "func": func,
            "plname": "%plugin_name%"
        })

        logger.info(f"Registered event. [Type: '{type}' Func: '{func.__name__}']", "EventImp Thread")
        
    def registerCommand(func):
        # import client.commands.EventsCommand as command; commands.cmds.append(command.Command)
        
        logger.warn("The command system is currently work in progress and might have a bug here and there :<", "Plugin-%plugin_name%")

        try:
            from csdata import commands
            
            aliases = func.aliases

            for alias in aliases:
                if alias in commands.aliases:
                    logger.error(f"A command with the name '{alias}' is already defined!", "Plugin-%plugin_name%")
                    return

            commands.cmds.append(func)
            
            logger.info(f"Registered command. [Class: '{func.__name__}']", "EventImp Thread")

        except Exception as e:
            logger.error(f"Failed to register command. [Class: '{func.__name__}']\\n{e}", "EventImp Thread")
            
    def registerCustomPacket(func):
        from csdata import packets
        logger.warn("The cpacket thng is also work in progress :D", "Plugin-%plugin_name%")

        try:
            type = func.type
            if packets.handlers.get(type):
                logger.error(f"Packet handler already exist [Func: '{func.__name__}']")
                return
        except:
            logger.error(f"Error while registering a custom packet! Type not set. [Func: '{func.__name__}']")
            return
        
        packets.pcks.append(func)
        for i in packets.pcks: packets.handlers[func.type] = i

        logger.info(f"Registered cpacket. [Type: '{type}' Func: '{func.__name__}']", "EventImp Thread")
        


def print(*args, **kwargs):
    pass