from scapy.all import *
from scapy.contrib.gtp import *

pkt = Ether(dst="96:ce:d1:9b:ef:8f",src="08:00:27:8b:7a:20") \
             /IP(dst="10.100.200.3",src="192.168.56.101")\
             /UDP()\
             /GTP_U_Header(teid=2,gtp_type=255)\
             /Ether()\
             /IP()

pkt.show()

sendp(pkt,iface="veth659e8a8")
