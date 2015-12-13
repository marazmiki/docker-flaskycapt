FROM marazmiki/cutycapt
MAINTAINER Mikhail Porokhovnichenko <marazmiki@gmail.com>
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update  -y && \
    apt-get install -y python python-pip python-dev build-essential xvfb xpra && \
    apt-get clean   -y


WORKDIR /app


COPY   entrypoint.sh      /app/entrypoint.sh
COPY   app.py             /app/app.py
COPY   requirements.txt   /app/requirements.txt


RUN    pip install -r /app/requirements.txt


EXPOSE 8765
ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
