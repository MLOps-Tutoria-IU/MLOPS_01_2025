FROM amazonlinux:latest AS base
RUN yum install -y python3.11 && \
    ln -sf /usr/bin/python3.11 /usr/bin/python && \
    curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py

FROM base AS build
COPY src /src
RUN pip install -r /src/requirements.txt

FROM build AS serving
CMD ["python", "/src/app.py"]