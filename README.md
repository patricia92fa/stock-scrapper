# Stock price scrapper
This repository contains python code that extracts stock data from various websites. The code is compiled and executed in a containerized environment designed with docker, ingested into an Elasticsearch database and visualized in a Kibana dashboard.

## Getting started
The only prerequisite is to have an updated Docker version installed. To do so, please follow the instructions of the [official documentation](https://docs.docker.com/install/linux/docker-ee/ubuntu/#install-using-the-repository).

To run the scrapper, just execute the `init.py` script located in the main folder. It will build the `Dockerfile`, execute the scrapper and save the extracted datasetin the `/csv` folder.
