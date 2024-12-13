# This file runs in the background and captures packets to export to a file.
# The captured packets are then displayed on a webpage.
# The packets are refreshed every 10 seconds.
# The packets are then displayed in a table with the following columns:
# Timestamp, MAC, SRC IP, SRC Port, DST IP, DST Port
# The packets are displayed in the order they were captured.
# The packets are captured using the pyshark library.
# The packets are captured using the eth0 interface.
# The packets are captured in real-time.
# The packets are captured continuously.

import pyshark
import time
from datetime import datetime

def capture_packets():
    while True:
        c = pyshark.LiveCapture(interface="eth0")
        packets = list(c.sniff_continuously(packet_count=50))
        with open("/app/livecapture.html", "w") as fo:
            fo.write("<html>\n")
            fo.write("<title>Captured Packets</title>\n")
            fo.write("<head>\n")
            fo.write("<link rel='stylesheet' type='text/css' href='/static/styles.css'>\n")
            fo.write("<meta http-equiv='refresh' content='10'>\n")  # Refresh the page every 10 seconds
            fo.write("</head>\n")
            fo.write("<body>\n")
            fo.write("<h1>Current Packets</h1>\n")
            fo.write("<nav>\n")
            fo.write("<a href='/packetcapture'>Packet Capture Page</a> | <a href='/livecapture'>Live Capture Page</a>\n")
            fo.write("</nav>\n")
            if packets:
                fo.write("<table id='packets'>\n")
                fo.write("<tr><th>Timestamp</th><th>MAC</th><th>SRC IP</th><th>DST IP</th><th>SRC Port</th><th>DST Port</th></tr>\n")
                for packet in packets:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    if hasattr(packet, 'eth') and hasattr(packet, 'ip'):
                        mac = packet.eth.addr
                        src_ip = packet.ip.src
                        dst_ip = packet.ip.dst
                        src_port = packet.tcp.srcport if hasattr(packet, 'tcp') else 'N/A'
                        dst_port = packet.tcp.dstport if hasattr(packet, 'tcp') else 'N/A'
                        fo.write(f"<tr><td>{timestamp}</td><td>{mac}</td><td>{src_ip}</td><td>{dst_ip}</td><td>{src_port}</td><td>{dst_port}</td></tr>\n")
                fo.write("</table>\n")
            else:
                fo.write("<h1>No packets have been captured</h1>\n")
            fo.write("</body>\n")
            fo.write("</html>\n")
        print("Updated livecapture.html")
        time.sleep(10)

# This function captures packets in real-time using the pyshark library.
# It captures packets from the eth0 interface and writes them to a file.
# The captured packets are displayed in an HTML table on a webpage.
# The webpage is refreshed every 10 seconds to show the latest packets.