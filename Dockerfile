FROM alpine:3.14

WORKDIR /app

COPY requirements.txt requirements.txt

RUN \
    apk add --update --no-cache python3 cmd:pip3 && \
    pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir --ignore-installed -r requirements.txt

COPY pelican pelican

WORKDIR /app/pelican

CMD ["pelican", "content"]
