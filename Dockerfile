FROM python:3.11.3-alpine

# Setup Portal
ADD src/requirements.txt /opt/src/requirements.txt
RUN pip3 install -r /opt/src/requirements.txt
ADD src /opt/src

RUN apk add --no-cache openssl

ADD entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
