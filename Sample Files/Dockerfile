# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install TShark and other necessary packages
RUN apt-get update && apt-get install -y tshark && apt-get install -y curl

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME=MrPacketCapture

# Run the packet capture script and the HTTP server when the container launches
CMD ["sh", "-c", "python capture_packets.py & python -m http.server 8000"]