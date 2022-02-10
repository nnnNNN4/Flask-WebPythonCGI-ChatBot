##データベース
FROM mysql:5.7
RUN touch /var/log/mysql/mysqld.log

ADD  ./mysql/my.cnf /etc/mysql/conf.d/my.cnf
RUN chmod 644 /etc/mysql/my.cnf
CMD ["mysqld"]

##Python本体
FROM python:3.6

ARG project_dir= /src

WORKDIR $project_dir

RUN apt-get update
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

RUN python -m pip install jupyterlab