FROM ubuntu:latest
MAINTAINER Juliano Resende Diniz "juliano.resende@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app", "-w", "4", "-t", "600", '--log-file', 'instance.log']