# pull official base image
FROM python:3.11

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set default shell
SHELL [ "/bin/bash", "-c" ]

# update/upgrade container & install git
RUN apt update && apt upgrade -y && apt install -y git

# clone the repository
RUN git clone https://github.com/hackerSa3edy/dockerized_terminal.git .

# set work directory
WORKDIR /dockerized_terminal

# install required packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
