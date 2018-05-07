FROM python:3.6.0

RUN apt-get update && apt-get -y install vim && rm -rf /var/lib/apt/lists/*

WORKDIR /home/app

ENV PYTHONPATH="/home/app" MYSQL_HOST="123.59.45.157" \
    MYSQL_DBNAME="jobsystem" MYSQL_USER="root" \
    MYSQL_PASSWD="root" MYSQL_PORT="30039"

EXPOSE 10011

COPY . /home/app/

RUN pip install -r requirements.txt

CMD ["python3", "run.py", "runserver"]