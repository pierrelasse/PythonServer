from csdata import cd
from utils import broadcast

# from event.joinEvent import Event as event_join
from plugin.pluginEvents import TriggerEvent

def Event(client):
    TriggerEvent("OnJoin", client)
    msg = f"{cd.clients_connected[client]['username']} joined the server"
    print(msg)
    broadcast(msg)