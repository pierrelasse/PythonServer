from csdata import packets


def LoadPackets():
    
    import client.packets.TestPacket as pck; packets.pcks.append(pck.Packet)
    
    for i in packets.pcks: packets.handlers[i.type] = i
    

def HandlePacket(type):
    for packet in packets.pcks:
        if packet.type == type:
            return packet.execute
    return 404

packets.load = LoadPackets
