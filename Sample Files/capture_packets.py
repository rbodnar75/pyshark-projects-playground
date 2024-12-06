import pyshark
import json
import time
from datetime import datetime

def capture_packets():
    while True:
        capture = pyshark.LiveCapture(interface='eth0')
        packets = []

        for packet in capture.sniff_continuously(packet_count=50):
            packet_info = {
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'mac': packet.eth.src if hasattr(packet, 'eth') else 'N/A',
                'src_ip': packet.ip.src if hasattr(packet, 'ip') else 'N/A',
                'dst_ip': packet.ip.dst if hasattr(packet, 'ip') else 'N/A',
                'src_port': packet.tcp.srcport if hasattr(packet, 'tcp') else 'N/A',
                'dst_port': packet.tcp.dstport if hasattr(packet, 'tcp') else 'N/A',
                'protocol': packet.transport_layer if hasattr(packet, 'transport_layer') else 'N/A',
                'info': str(packet)
            }
            packets.append(packet_info)

        # Save packets to JSON file
        with open('/app/packets.json', 'w') as f:
            json.dump(packets, f, indent=4)

        # Save packets to PCAP file
        capture_file = pyshark.FileCapture('/app/packets.pcap', mode='w')
        for packet in packets:
            capture_file.write(packet)
        capture_file.close()

        print("Updated packets.json and packets.pcap")
        time.sleep(10)

if __name__ == '__main__':
    capture_packets()