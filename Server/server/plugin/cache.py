from csdata import plugins
from log import logger

def setcache(plugin, path, value):
    try:
        if not plugins.cache.get(plugin):
            plugins.cache[plugin] = {}

        plugins.cache[plugin][path] = value
    except Exception as e:
        logger.error(f"Error while setting cache value [{plugin}:{path}]:\\n{e}")

def getcache(plugin, path):
    value = "null"
    try:
        value = plugins.cache[plugin][path]
    except:
        pass
    return value
