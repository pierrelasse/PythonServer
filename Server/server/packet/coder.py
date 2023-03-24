import json

# from packet.coder import PacketCoder as packet

class PacketCoder:
    def decode(packet):
        if not packet:
            return
        try:
            packet = packet.decode('utf-8')
        except:
            pass
        try:
            packet = json.loads(packet)
        except:
            return {}
        return packet
    
    def load(packet):
        try:
            packet = packet.decode('utf-8')
            packet = json.loads(packet)
        except:
            return {}
        return packet
    
    def gvfp(packet, value):
        v = "null"
        try:
            v = packet[value]
        except:
            pass
        return v
    
    def gen(type, **kwargs):
        packet = {"type": type}
        for arg in kwargs:
            packet[arg] = kwargs[arg]
        return json.dumps(packet).encode('utf-8')