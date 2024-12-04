sudo docker stop mrpacket
sudo docker rm mrpacket
sudo docker build -t packetcapture-webserver .
sudo docker run -d --name mrpacket --cap-add=NET_ADMIN -p 5001:5001 packetcapture-webserver
