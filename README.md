# Stock price scrapper
This repository contains python code that extracts stock data from various websites. The code is compiled and executed in a containerized environment designed with docker, ingested into an Elasticsearch database and visualized in a Kibana dashboard.

## Getting started
To run the scrapper, just execute the `init.py` script located in the main folder. It will build the `Dockerfile` and run the resulting image, which in turn runs the web scrapping code periodically, ingests the data intro an Elasticsearch data node.The Kibana dashboard is then available at `localhost:5601`.

### Content description
* **/docker/Dockerfile**
* **/docker/requirements.txt**
* **/src/stock\_scrap.py**
* **/csv/stock\_data.csv**
* **/pdf/respuestas.pdf**

## Author
Patricia Ferreiro

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Resources
1. Lawson, R. (2015). _Web Scraping with Python_. Packt Publishing Ltd. Chapter 2. Scraping the Data.
2. Mitchel, R. (2015). _Web Scraping with Python: Collecting Data from the Modern Web_. O'Reilly Media, Inc. Chapter 1. Your First Web Scraper.
