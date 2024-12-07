# pyshark-projects-playground

This repository is a playground for testing different Python scripts using Pyshark. The primary focus is on utilizing a web server to capture and display network packets.

Before you can use any of these scripts, you will need to install **Pyshark**.

***Note: It may be necessary to change the interface in the sample files***

The setup instructions for **Pyshark** can be found at the following repo:
https://github.com/KimiNewt/pyshark.git

***Note: This project is still in its early stages. Use with caution.***


## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/rbodnar75/pyshark-projects-playground.git
   cd pyshark-projects-playground
   ```

2. **Install Dependencies**
   Ensure you have Docker installed on your system. Then, build the Docker image:
   ```bash
   docker build -t packetcapture .
   ```

3. **Run the Docker Container**
   ```bash
   docker run -p 5001:5001 packetcapture
   ```

## Usage

### Running the Web Server

The web server is built using Flask and is configured to capture packets and display them on a web page. To start the server, follow the instructions under Installation.

### Capturing Packets

The server continuously captures packets using Pyshark and updates the `packetcapture.html` file with the latest packet information. The packet details include:
- MAC Address
- Source IP
- Destination IP
- Source Port
- Destination Port
- Protocol

### Accessing the Web Interface

Open your web browser and navigate to `http://localhost:5001`. You will see the captured packets displayed on the web page. The page refreshes every 10 seconds to show the latest captured packets.

## Example Output

Here is a sample of what the captured packets might look like on the web interface:

![Packet Capture](path/to/screenshot.png)

## Key Files

- `Sample Files/app.py`: The main Flask application that sets up the web server and handles packet capturing.
- `Sample Files/capture_packets.py`: Script for capturing packets and saving them in JSON and PCAP formats.
- `Sample Files/Dockerfile`: Dockerfile for setting up the environment and running the application.
- `Sample Files/packetcapture.html`: HTML template for displaying captured packets.

## License

This project is licensed under the MIT License.

For more information, visit the [repository](https://github.com/rbodnar75/pyshark-projects-playground).
