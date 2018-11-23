FROM python:3.7.1-alpine3.8

RUN apk update && apk add nginx

RUN adduser -D -g 'www' www
RUN mkdir /www
RUN chown -R www:www /var/lib/nginx
RUN chown -R www:www /www

RUN mv etc/nginx/nginx.conf /etc/nginx/nginx.conf.orig
COPY ./nginx.conf /etc/nginx/nginx.conf

RUN chmod -R 777 /var/tmp/

RUN apk add build-base linux-headers pcre-dev
RUN apk --update add build-base libffi-dev python-dev py-pip
RUN pip install --upgrade pip
RUN apk add git

RUN pip install https://github.com/unbit/uwsgi/archive/uwsgi-2.0.zip#egg=uwsgi

RUN apk add --no-cache openssh
RUN apk add --no-cache libxslt-dev
RUN apk add xmlsec-dev

COPY ./requirements.txt /var/requirements.txt
RUN pip install -r /var/requirements.txt
RUN rm /var/requirements.txt

RUN mkdir /var/www/python-intro
RUN mkdir /var/log/uwsgi
RUN touch /var/log/uwsgi/python-intro.log

WORKDIR /var/www/python-intro
ENV PYTHONPATH=/var/www/python-intro

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]