import pyshark
from datetime import datetime

def capture_malformed_packets():
    # Create or open the HTML file in append mode
    with open("malformed_packets.html", "a") as fo:
        # Write the initial HTML structure if the file is empty
        if fo.tell() == 0:
            fo.write("<html>\n")
            fo.write("<title>Malformed Packets</title>\n")
            fo.write("<head>\n")
            fo.write("<style>\n")
            fo.write("#packets {  font-family: Arial, Helvetica, sans-serif;  border-collapse: collapse;  width: 100%;}")
            fo.write("#packets td, #packets th {  border: 1px solid #ddd;  padding: 8px;}")
            fo.write("#packets tr:nth-child(even){background-color: #f2f2f2;}")
            fo.write("#packets tr:hover {background-color: #ddd;}")
            fo.write("#packets th {  padding-top: 12px;  padding-bottom: 12px;  text-align: left;  background-color: #0757a2;  color: white;}")
            fo.write("</style>\n")
            fo.write("</head>\n")
            fo.write("<body>\n")
            fo.write("<table id='packets'>\n")
            fo.write("<tr><th>Timestamp</th><th>SRC IP</th><th>SRC Port</th><th>DST IP</th><th>DST Port</th></tr>\n")

        # Capture packets with a filter for malformed packets
        c = pyshark.LiveCapture(interface="Wi-Fi", bpf_filter="ip and tcp")
        for packet in c.sniff_continuously():
            if hasattr(packet, 'malformed'):
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                src_ip = packet.ip.src
                dst_ip = packet.ip.dst
                src_port = packet.tcp.srcport
                dst_port = packet.tcp.dstport
                fo.write(f"<tr><td>{timestamp}</td><td>{src_ip}</td><td>{src_port}</td><td>{dst_ip}</td><td>{dst_port}</td></tr>\n")

        # Close the HTML structure
        fo.write("</table>\n")
        fo.write("</body>\n")
        fo.write("</html>\n")

if __name__ == "__main__":
    capture_malformed_packets()