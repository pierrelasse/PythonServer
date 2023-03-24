from _thread import start_new_thread
import traceback

from csdata import plugins

from log import logger

def TriggerEvent(e, *args, **kwargs):
    start_new_thread(_TriggerEvent, (e, kwargs))

def _TriggerEvent(e, *args, **kwargs):
    for event in plugins.revents:
        if event['event'] == e:
            try:
                event['func'](kwargs)
            except Exception as e:
                logger.error(f"Error while executing event from plugin {event['plname']}:\n  {e}")
                traceback.print_exc()
                