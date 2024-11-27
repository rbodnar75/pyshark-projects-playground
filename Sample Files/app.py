from flask import Flask, send_file, make_response
import pyshark
import threading
import time
from datetime import datetime

app = Flask(__name__)

def capture_packets():
    while True:
        c = pyshark.LiveCapture(interface="eth0")
        packets = list(c.sniff_continuously(packet_count=50))
        with open("packetcapture.html", "w") as fo:
            fo.write("<html>\n")
            fo.write("<title>Captured Packets</title>\n")
            fo.write("<head>\n")
            fo.write("<style>\n")
            fo.write("#packets {  font-family: Arial, Helvetica, sans-serif;  border-collapse: collapse;  width: 100%;}")
            fo.write("#packets td, #packets th {  border: 1px solid #ddd;  padding: 8px;}")
            fo.write("#packets tr:nth-child(even){background-color: #f2f2f2;}")
            fo.write("#packets tr:hover {background-color: #ddd;}")
            fo.write("#packets th {  padding-top: 12px;  padding-bottom: 12px;  text-align: left;  background-color: #0757a2;  color: white;}")
            fo.write("body {\n")
            fo.write("background-color: lightblue;\n")
            fo.write("}\n")
            fo.write("h1 {\n")
            fo.write("  font-family: Arial, Helvetica, sans-serif;\n")
            fo.write("  color: white;\n")
            fo.write("  text-align: center;\n")
            fo.write("}\n")
            fo.write("p {\n")
            fo.write("  font-family: Arial, Helvetica, sans-serif;\n")
            fo.write("  font-size: 20px;\n")
            fo.write("  text-align: center;\n")
            fo.write("}\n")
            fo.write("</style>\n")
            fo.write("</head>\n")
            fo.write("<body>\n")        
            fo.write("<h1>Current Packets</h1>\n")
            fo.write("<p>\n")

            if packets:
                fo.write("<table id='packets'>\n")
                fo.write("<tr><th>Timestamp</th><th>MAC</th><th>SRC IP</th><th>DST IP</th></tr>\n")
                for packet in packets:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    if hasattr(packet, 'eth') and hasattr(packet, 'ip'):
                        fo.write(f"<tr><td>{timestamp}</td><td>{packet.eth.addr}</td><td>{packet.ip.src}</td><td>{packet.ip.dst}</td></tr>\n")
                fo.write("</table>\n")
            else:
                fo.write("<h1>No packets have been captured</h1>\n")
            fo.write("</p>\n")
            fo.write("</body>\n")
            fo.write("</html>\n")
        print("Updated packetcapture.html")
        time.sleep(30)

@app.route('/')
def home():
    response = make_response(send_file("packetcapture.html"))
    response.headers['Cache-Control'] = 'no-store'
    return response

if __name__ == '__main__':
    # Start the packet capture in a separate thread
    capture_thread = threading.Thread(target=capture_packets)
    capture_thread.daemon = True
    capture_thread.start()
    
    # Start the Flask web server on a different port, e.g., 5001
    app.run(host='0.0.0.0', port=5001)