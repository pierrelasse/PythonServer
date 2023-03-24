from csdata import cd

from packet.coder import PacketCoder as packet

from utils import getusername, getaddress, broadcast, isclientconnected

# from disconnect import disconnect
from event.quitEvent import Event as event_quit

def disconnect(client, reason="", silent=False, supersilent=False):
    try:
        if not client.fileno() == -1:
            execute(client, reason, silent, supersilent)
    except:
        pass
    
    try:
        client.close()
    except:
        pass

def execute(client, reason="", silent=False, supersilent=False):
    if not len(reason) > 0:
        reason = "Disconnected"
        
    isconnected = isclientconnected(client)
    username = getusername(client)
    
    if supersilent == True:
        silent = True
    else:
        print(f"{username}[/{getaddress(client)}] lost connection: {reason}")
    
    if isconnected == True:
        client.send(packet.gen("disconnect", error=reason))
    

    if silent == False:
        event_quit(client)
        
    #event_quit(client)
    


#cd.clients_connected[client] = None