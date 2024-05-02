FROM python:3.8

RUN apt update
RUN apt install python3-pip -y
RUN pip install --upgrade pip


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app

COPY . .

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]