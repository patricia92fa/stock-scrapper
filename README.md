# Stock price scrapper
This repository contains a Python3 web scrapper that extracts live stock data from the 'Yahoo Finanzas' web service.

## Getting started
The only prerequisite is to have an updated Docker version installed. To do so, please follow the instructions of the [official documentation](https://docs.docker.com/install/linux/docker-ee/ubuntu/#install-using-the-repository).

To run the scrapper, just execute the `build.sh` and `run.sh` scripts, both located in the root directory of this repository. It will build the `Dockerfile` (which includes all dependencies) located at `/src`, execute the scrapper found at `/src/stock.py` and save the extracted dataset in the `/csv` folder.
