FROM php:7-apache

COPY ./vsim.com /var/www/html

WORKDIR /app/VSIM

COPY ./VSIM /app/VSIM

RUN chown -R www-data:www-data /app && \
  chmod -R g+w /app

RUN apt-get update && \
  apt-get install -y bedtools

RUN apt-get install -y python3 python3-pip
