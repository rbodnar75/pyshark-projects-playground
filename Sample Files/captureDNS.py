   for packet in capture.sniff_continuously(packet_count=10):
       if 'DNS' in packet:
           print(packet.dns.qry_name)