echo "Stopping current mrpacketcapture container"
sudo docker stop mrpacketcapture
echo ". . . stopped"
echo "Removing current mrpacketcapture container"
sudo docker rm mrpacketcapture
echo ". . . removed"
echo "Building new mrpacketcapture image"
sudo docker build -t mrpacketcapture .
echo "mrpacket . . . built"
echo "Running new mrpacket container"
sudo docker run -d --name mrpacketcapture --cap-add=NET_ADMIN -p 8000:8000 -v /home/rbodnar/pyshark-projects-playground/data:/app/data mrpacketcapture
#sudo docker run -d --name mrpacketcapture --cap-add=NET_ADMIN -p 8000:8000 -v /data:/app/data mrpacketcapture
echo "mrpacket . . . running"