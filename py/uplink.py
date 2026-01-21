from scapy.all import *
from scapy.contrib.gtp import *

pkt = Ether(dst="00:11:22:33:44:55",src="55:44:33:22:11:00") \
             /IP(dst="10.100.200.3",src="192.168.56.101")\
             /UDP()\
             /GTP_U_Header(teid=2,gtp_type=255)\
             /Ether()\
             /IP()

pkt.show()

sendp(pkt,iface="<if name>")
