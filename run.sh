#sudo docker run -v $(pwd)/csv:/data stock-scrapper:latest
sudo docker run --shm-size 4g -v $(pwd)/csv:/data stock-scrapper:latest
