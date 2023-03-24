import os
import json
import traceback
import time
import random

from csdata import pd, plugins

from plugin.pluginExceptions import *

from log import logger
from log import logger as _log

from utils import sendto as _sendto

class Plugin:
    def __init__(self):
        self.root = pd.path['pluginroot']

        for plugin in os.listdir(self.root):
            try:
                self.loadplugin(os.path.join(self.root, plugin))
            except NoIndexFile as e:
                logger.error(f"No index file was found! [{e}]", "Plugin Thread")

            except FailedToLoadIndex as e:
                logger.error(f"Failed to load index file: {e}", "Plugin Thread")
                
            except InvalidArguments as e:
                logger.error(f"Invalid arguments: {e}", "Plugin Thread")
                
            except PluginAlreadyLoaded as e:
                logger.error(f"The plugin {e} was already loaded!", "Plugin Thread")
    
    

    def loadplugin(self, path):
        index = os.path.normpath(path + "\\index.json")

        if not os.path.isfile(index):
            raise NoIndexFile(index)

        try:
            with open(index, 'r') as f:
                index = json.load(f)

        except Exception as e:
            raise FailedToLoadIndex("Failed while decoding file. " + str(e))

        plugin_version = "null"
        try:
            plugin_name = index['name']
            plugin_version = index['version']
            plugin_index = index['index']
            plugin_index_path = os.path.normpath(f"{path}\\{plugin_index}")
        except:
            pass
        
        if plugin_name in plugins.lp:
            raise PluginAlreadyLoaded(plugin_name)
        
        if not 3 <= len(plugin_name) <= 27:
            foldername = path.split('\\')[-1]
            raise InvalidArguments(f"Invalid plugin name. Name too long (3-27) [{foldername}]")

        if not os.path.isfile(plugin_index_path):
            raise InvalidArguments(f"No enter file found. [{plugin_index_path}]")
        
        logger.info(f"&<A709D4>Loading plugin {plugin_name} version {plugin_version}. Index: {plugin_index}", "Plugin-Loader Thread", "&")

        plugins.lp[plugin_name] = {}
        plugins.lp[plugin_name]['version'] = plugin_version
        plugins.lp[plugin_name]['index'] = plugin_index
        plugins.lp[plugin_name]['index_path'] = plugin_index_path
        
        try:
            self.runplugin(plugin_index_path, plugin_name)
        except Exception as e:
            logger.error(f"An exception occurred while running plugin {plugin_name}:", "Plugin-Loader Thread", "&")
            traceback.print_exc()
        
        logger.info(f"&<5AAD4C>Started plugin {plugin_name}!", "Plugin-Loader Thread", "&")
        
    def runplugin(self, path, name="null"):
        if name == "null":
            return
                
        time.sleep(random.randint(1, 15) / 100)

        logger.info(f"&dExecuting plugin {name}", "Plugin-Executor Thread", "&")
        
        with open(path) as hehehaha:
            hehehaha = hehehaha.read()
            
        if not hehehaha:
            return
        
        exec(pluginimports.replace("%plugin_name%", str(name)))

        self = None
        pd = None

        exec(hehehaha.replace("%plugin_name%", str(name)))
        
        time.sleep(random.randint(1, 60) / 100)
        


pluginimports = """
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
            if type in packets.handlers:
                logger.error(f"Packet handler already exist [Func: '{func.__name__}']")
                return
        except:
            logger.error(f"Error while registering a custom packet! Type not set. [Func: '{func.__name__}']")
            return
        
        packets.pcks.append(func)
        for i in packets.pcks:
            packets.handlers[func.type] = i

        logger.info(f"Registered cpacket. [Type: '{type}' Func: '{func.__name__}']", "EventImp Thread")
        


def print(*args, **kwargs):
    pass
"""