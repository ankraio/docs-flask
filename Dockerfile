FROM python:3.13.0a3-alpine

RUN apk add build-base libffi-dev openssl-dev python3-dev

# Setup Example
ADD src/requirements.txt /opt/src/requirements.txt
RUN pip3 install -r /opt/src/requirements.txt
ADD src /opt/src

RUN apk add --no-cache openssl

ADD entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
