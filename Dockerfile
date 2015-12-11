FROM python:3.5
#FROM python:3-onbuild
#ENV PYTHONUNBUFFERED 1

ENV DEBIAN_FRONTEND noninteractive

ENV HTTP_PROXY="http://myproxy.redaelli.org:80"
ENV HTTPS_PROXY="http://myproxy.redaelli.org:80"
ENV http_proxy="http://myproxy.redaelli.org:80"
ENV https_proxy="http://myproxy.redaelli.org:80"
ENV PIP_OPTIONS="--proxy $HTTP_PROXY"

COPY requirements.txt /usr/src/app/
COPY app.py /usr/src/app/

WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y nmap
RUN pip install --proxy $HTTP_PROXY --no-cache-dir -r requirements.txt

VOLUME ["/usr/src/app"]
EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["./app.py"]
