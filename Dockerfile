FROM python:3.9
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN pip install numpy==1.26.4
RUN pip install pyopenssl==22.0.0
RUN apt-get update && apt-get install -y wget unzip && \
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
apt install -y ./google-chrome-stable_current_amd64.deb && \
apt-get clean


CMD ["python3", "main.py"]