import pyshark
import json
import time
from datetime import datetime

def capture_packets():
    packets = []

    while True:
        new_packets = []
        capture = pyshark.LiveCapture(interface='eth0')
        capture.sniff(packet_count=50)

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
            new_packets.append(packet_info)

        packets.extend(new_packets)

        # Save packets to both a JSON file and a PCAP file
        with open('/app/data/packets.json', 'w') as f:
            json.dump(list(packets), f, indent=4)

        # Save packets to PCAP file
        capture = pyshark.LiveCapture(interface='eth0', output_file='/app/data/packets.pcap')
        capture.sniff(packet_count=50)

        print("Updated packets.json and packets.pcap")
        time.sleep(10)

if __name__ == '__main__':
    capture_packets()