FROM python:3.6.0

RUN apt-get update && apt-get -y install vim && rm -rf /var/lib/apt/lists/*

WORKDIR /home/app

ENV PYTHONPATH /home/app

EXPOSE 10012 10011

COPY . /home/app/

RUN pip3 install -r requirements.txt

CMD ["python3", "run.py", "runserver"]