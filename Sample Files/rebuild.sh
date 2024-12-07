echo "Stopping current mrpacket container"
sudo docker stop mrpacket
echo ". . . stopped"
echo "Removing current mrpacket container"
sudo docker rm mrpacket
echo ". . . removed"
echo "Building new mrpacket container"
sudo docker build -t mrpacketcapture .
echo "mrpacket . . . built"
echo "Running new mrpacket container"
sudo docker run -d --name mrpacket --cap-add=NET_ADMIN -p 8000:8000 packetcapture
echo "mrpacket . . . running"
