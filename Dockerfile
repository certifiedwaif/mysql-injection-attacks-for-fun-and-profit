FROM ubuntu
RUN apt-get update
RUN apt-get install -y wait-for-it \
                        mysql-client \
                        libmysqlclient-dev \
                        python3 \
                        python3-pip
RUN adduser user
USER user
WORKDIR /app
RUN pip3.10 install mysql-connector-python
COPY ./mysql_client.py /app
CMD ["wait-for-it", "mysql-server:3306", "--", "python3", "mysql_client.py"]
