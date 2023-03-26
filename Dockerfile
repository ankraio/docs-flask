FROM registry.infra.ankra.cloud/alpine/python3:11

# Setup Portal
ADD src/requirements.txt /opt/src/requirements.txt
RUN pip3 install -r /opt/src/requirements.txt
ADD src /opt/src

RUN apk add --no-cache openssl

RUN curl https://bitbucket.org/api/2.0/snippets/stmercury/nxdkRz/a86e24b5491b68fb58aaa000f5187e4bacdff8bc/files/ankra_dev_root_ca.crt >> /etc/ssl/certs/ca-certificates.crt

ADD entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
