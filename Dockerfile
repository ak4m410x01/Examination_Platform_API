FROM python:3.11
SHELL [ "/bin/bash","-c" ]
RUN apt update && apt upgrade -y
RUN pip install --upgrade pip
ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app
ADD . .
RUN pip install -r requirements.txt

RUN chmod +x django_entrypoints.sh