FROM python:2.7
ENV http_proxy 144.66.6.175:3128/
ENV https_proxy 144.66.6.175:3128/
ADD . /code
WORKDIR /code
RUN pip install Django
EXPOSE 9876

