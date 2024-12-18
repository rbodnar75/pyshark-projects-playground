# Packet Capture Application

This project is a network packet capture application built using Python, Flask, and the PyShark library. It captures network packets in real-time and provides a web interface to view and analyze the captured data.

## Project Structure

```
packet-capture-app
├── src
│   ├── capture_packets.py      # Captures network packets and serves them via Flask
│   ├── static
│   │   └── styles.css          # CSS styles for the web application
│   ├── templates
│   │   ├── index.html          # Main HTML page displaying captured packet data
│   │   └── stats.html          # HTML page displaying statistics about captured packets
│   └── app.py                  # Entry point of the Flask application
├── Dockerfile                   # Dockerfile for building the application image
├── requirements.txt             # Python dependencies for the project
└── README.md                    # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd packet-capture-app
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   Start the Flask application by running:
   ```
   python src/app.py
   ```
   The application will be accessible at `http://localhost:8000`.

4. **Using Docker:**
   To build and run the application using Docker, execute the following commands:
   ```
   docker build -t packet-capture-app .
   docker run -p 8000:8000 packet-capture-app
   ```

## Usage

- Navigate to the main page to view captured packet data and use the filtering options.
- Access the statistics page to view insights about the captured packets, such as counts by source and destination IPs and port usage.

## License

This project is licensed under the MIT License. See the LICENSE file for details.