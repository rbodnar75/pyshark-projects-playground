# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install TShark
RUN apt-get update && apt-get install -y tshark

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Define environment variable
ENV NAME=PacketCaptureWebServer

# Run both app.py and capturingpackets.py when the container launches
CMD ["sh", "-c", "python capturingpackets.py & python app.py"]