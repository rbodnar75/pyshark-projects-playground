from flask import Flask, render_template
import json

app = Flask(__name__)

def load_packets():
    with open('/app/data/packets.json') as f:
        return json.load(f)

@app.route('/stats')
def stats():
    packets = load_packets()
    
    total_packets = len(packets)
    src_ip_count = {}
    dst_ip_count = {}
    port_count = {}

    for packet in packets:
        src_ip = packet['src_ip']
        dst_ip = packet['dst_ip']
        src_port = packet['src_port']
        dst_port = packet['dst_port']

        # Count source IPs
        if src_ip in src_ip_count:
            src_ip_count[src_ip] += 1
        else:
            src_ip_count[src_ip] = 1

        # Count destination IPs
        if dst_ip in dst_ip_count:
            dst_ip_count[dst_ip] += 1
        else:
            dst_ip_count[dst_ip] = 1

        # Count source ports
        if src_port in port_count:
            port_count[src_port] += 1
        else:
            port_count[src_port] = 1

        # Count destination ports
        if dst_port in port_count:
            port_count[dst_port] += 1
        else:
            port_count[dst_port] = 1

    return render_template('stats.html', total_packets=total_packets, src_ip_count=src_ip_count, dst_ip_count=dst_ip_count, port_count=port_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)