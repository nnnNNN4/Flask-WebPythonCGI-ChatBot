##データベース
FROM mysql:5.7
RUN touch /var/log/mysql/mysqld.log
RUN touch /run/mysqld/mysqld.sock
RUN touch /var/log/mysql/mysqld.log
RUN apt-get install default-mysql-client

COPY ./mysql/conf.d/my.cnf /etc/mysql/conf.d/my.cnf
RUN chmod 644 /etc/mysql/my.cnf
CMD ["mysqld"]

##アプリケーション
FROM python:3.8

ADD . /Flask-Project-1/src
WORKDIR /Flask-Project-1/src
RUN pip install -r requirements.txt

WORKDIR /Flask-Project-1
CMD sh start.sh

RUN apt-get update && apt upgrade -y
RUN apt install -y nodejs npm && npm install
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools