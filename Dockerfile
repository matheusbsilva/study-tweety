FROM python:3

RUN mkdir /tweety
WORKDIR /tweety/

ADD requirements.txt /tweety/

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

ADD . /tweety/



