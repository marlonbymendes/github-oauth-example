FROM python:3.6.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
COPY requirements.txt /code/requirements.txt
COPY github_oauth/* /code/
WORKDIR /code
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
