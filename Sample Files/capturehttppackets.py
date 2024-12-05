for packet in capture.sniff_continuously(packet_count=10):
       if 'HTTP' in packet:
           print(packet.http)