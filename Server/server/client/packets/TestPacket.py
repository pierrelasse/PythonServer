
class Packet:
    type = "test"
    
    def execute(source, p):
        print("abc")
        from packet.coder import PacketCoder as packet
        from utils import sendto
        
        value = packet.gvfp(p, "arg")

        sendto(source, f"LOLOLOLOLOLOLO OMFG EPIK TEST PACKET! Value: {value}")
