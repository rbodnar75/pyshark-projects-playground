import xml.etree.ElementTree as ET
import pandas as pd

def parse_nmap_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()
    data = []
    hosts_count = len(root.findall('.//host'))
    print(f"Found {hosts_count} hosts in scan")

    for host in root.findall('host'):
        ip = host.find('address').get('addr')
        ports_elem = host.find('ports')
        if ports_elem is None:
            print(f"No ports found for host {ip}")
            continue
            
        for port in ports_elem.findall('port'):
            port_id = port.get('portid')
            protocol = port.get('protocol')
            state = port.find('state').get('state')
            service_elem = port.find('service')
            service = service_elem.get('name') if service_elem is not None else 'unknown'
            data.append([ip, port_id, protocol, state, service])

    if not data:
        print("Warning: No port data found in scan results")
        return pd.DataFrame(columns=['IP', 'Port', 'Protocol', 'State', 'Service'])
        
    return pd.DataFrame(data, columns=['IP', 'Port', 'Protocol', 'State', 'Service'])

df = parse_nmap_xml('nmap_scan.xml')
print(df.head())

from sklearn.ensemble import IsolationForest

# Prepare the data for the model
df['Port'] = df['Port'].astype(int)
df['Anomaly'] = 0  # Initialize anomaly column

# Convert categorical data to numerical
df = pd.get_dummies(df, columns=['Protocol', 'State', 'Service'])

# Train the Isolation Forest model
model = IsolationForest(contamination=0.1)
df['Anomaly'] = model.fit_predict(df.drop(columns=['IP', 'Anomaly']))

# Filter out anomalies
anomalies = df[df['Anomaly'] == -1]
print("Anomalies detected:")
print(anomalies)