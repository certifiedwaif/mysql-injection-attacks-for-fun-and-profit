FROM ubuntu
RUN apt-get update
RUN apt-get install -y wait-for-it \
                        mysql-client \
                        libmysqlclient-dev \
                        python3 \
                        python3-pip
RUN pip install mysql
WORKDIR /app
COPY ./mysql_client.py /app
CMD ["wait-for-it", "mysql-server:3306", "--", "mysql", "-hmysql-server", "-uuser", "-p"]
