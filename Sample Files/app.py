from flask import Flask, send_file
import pyshark
import threading
import time

app = Flask(__name__)

def capture_packets():
    while True:
        c = pyshark.LiveCapture(interface="any")
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
            fo.write("</style>\n")
            fo.write("</head>\n")
            fo.write("<body>\n")
            fo.write("<table id='packets'>\n")
            fo.write("<tr><th>MAC</th><th>SRC IP</th><th>DST IP</th></tr>\n")
            for packet in c.sniff_continuously(packet_count=50):
                fo.write(f"<tr><td>{packet.eth.addr}</td><td>{packet.ip.addr}</td><td>{packet.ip.dst}</td></tr>\n")
            fo.write("</table>\n")
            fo.write("</body>\n")
            fo.write("</html>\n")
        time.sleep(30)

@app.route('/')
def home():
    return send_file("packetcapture.html")

if __name__ == '__main__':
    # Start the packet capture in a separate thread
    capture_thread = threading.Thread(target=capture_packets)
    capture_thread.daemon = True
    capture_thread.start()
    
    # Start the Flask web server
    app.run(host='0.0.0.0', port=5000)