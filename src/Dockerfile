FROM ubuntu:16.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe
RUN apt-get update && apt-get install -y \
    apache2 \
    curl \
    git \
    python3.4 \
    python3-pip

# Add required files
ADD requirements.txt requirements.txt
ADD stock_scrap.py /usr/lib/python3.5/stock_scrap.py

# Install required pip packages
RUN chmod +x /usr/lib/python3.5/stock_scrap.py 
RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt

# Execute python code
RUN mkdir data
CMD ./usr/lib/python3.5/stock_scrap.py
#CMD /bin/sh -c
