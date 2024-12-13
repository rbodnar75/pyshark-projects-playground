from flask import Flask, send_file, make_response, jsonify
import pyshark
import threading
import time
from datetime import datetime

app = Flask(__name__)

def capture_packets():
    while True:
        c = pyshark.LiveCapture(interface="eth0")
        packets = list(c.sniff_continuously(packet_count=50))
        with open("/app/packetcapture.html", "w") as fo:
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
        print("Updated packetcapture.html")
        time.sleep(10)

@app.route('/')
def home():
    try:
        response = make_response(send_file("/app/packetcapture.html"))
        response.headers['Cache-Control'] = 'no-store'
        return response
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/packetcapture')
def packetcapture():
    try:
        response = make_response(send_file("/app/packetcapture.html"))
        response.headers['Cache-Control'] = 'no-store'
        return response
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/livecapture')
def livecapture():
    try:
        response = make_response(send_file("/app/livecapture.html"))
        response.headers['Cache-Control'] = 'no-store'
        return response
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    # Start the packet capture in a separate thread
    capture_thread = threading.Thread(target=capture_packets)
    capture_thread.daemon = True
    capture_thread.start()
    
    # Start the Flask web server
    app.run(host='0.0.0.0', port=5001)