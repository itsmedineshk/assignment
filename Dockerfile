FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY video_club /code/video_club
#COPY requirements.txt /code/
RUN pip3 install -r /code/video_club/requirements.txt
