FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y emacs

RUN pip3 install flask
RUN pip3 install --upgrade flask
RUN pip3 install mysql-connector-python
RUN pip3 install flask_cors
RUN pip3 install pytest
RUN pip3 install elasticsearch
RUN pip3 install neo4j

ENV APP_PATH=/home/src
WORKDIR $APP_PATH
ENV HOME $APP_PATH
ENV PYTHONPATH $APP_PATH
ENV FLASKPATH $APP_PATH/src

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENV MYSQL_DATABASE=keyword
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password

CMD ["flask", "run",  "--host" ,"0.0.0.0" ,"--port",  "5000"]
