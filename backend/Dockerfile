FROM python:3.9.14-buster
    MAINTAINER gokulakrishnan <gokulakams@gmail.com>
RUN echo 'Acquire::HTTP::Proxy "http://172.17.0.1:3142";' >> /etc/apt/apt.conf.d/01proxy \
 && echo 'Acquire::HTTPS::Proxy "false";' >> /etc/apt/apt.conf.d/01proxy## python specific
RUN    apt update
EXPOSE 443
WORKDIR /app
# python version change
COPY ./app/requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY ./app/ .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
VOLUME /var/run/docker.sock
