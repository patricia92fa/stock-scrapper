FROM ubuntu:16.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe
RUN apt-get update && apt-get install -y \
    apache2 \
    curl \
    git \
    wget \
    firefox \
    dbus-x11 \
    xvfb \
    python3.4 \
    python3-pip

# Install geckodrive 
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.20.0/geckodriver-v0.20.0-linux64.tar.gz \
  && tar xf geckodriver* \
  && chmod +x geckodriver \
  && export PATH=$PATH:$(pwd)/geckodrive \
  && mv geckodriver /usr/local/bin

# Install required pip packages
ADD requirements.txt requirements.txt
RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt

# Add required files
ADD stock.py /usr/lib/python3.5/stock.py
RUN chmod +x /usr/lib/python3.5/stock.py


# Execute python code
RUN mkdir data
ENV DISPLAY :1.0 
CMD Xvfb :1 -screen 0 800x600x16 & ./usr/lib/python3.5/stock.py
