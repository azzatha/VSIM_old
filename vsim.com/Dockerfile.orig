FROM httpd
FROM ubuntu:14.04
FROM biocontainers/biocontainers:latest


LABEL maintainer <azza.althagafi@kaust.edu.sa>

USER root
WORKDIR /opt


COPY . /usr/local/apache2/htdocs/

ENV DEBIAN_FRONTEND noninteractive

# Install all the requirements

RUN apt-get update && apt-get install -y \
        wget \
        unzip \
        build-essential \
        zlib1g-dev \
        libncurses5-dev \
        git 
        
# Python 3
RUN apt-get update  \
  && apt-get install -y tabix \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip 

  
# Miniconda3 and # vcfanno https://conda.io/miniconda.html
RUN apt-get install wget tar ca-certificates -y
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN chmod +x Miniconda3-latest-Linux-x86_64.sh 
ENTRYPOINT ./Miniconda3-latest-Linux-x86_64.sh 
RUN apt-get install -y libgl1-mesa-glx apt-utils openssh-server net-tools

#install vcfanno
RUN wget https://github.com/brentp/vcfanno/releases/download/v0.3.1/vcfanno_linux64
RUN chmod a+x vcfanno_linux64
RUN ln -s vcfanno_linux64 vcfanno
ENV PATH "$PATH:/opt"
RUN echo "[vcfanno]" >> /opt/versions
RUN vcfanno 2>&1 | grep "version" >> /opt/versions


# bedtools http://bedtools.readthedocs.io/en/latest/content/installation.html
RUN conda install bedtools=2.27.1
WORKDIR /data/
CMD ["bedtools"]

#RUN wget https://github.com/arq5x/bedtools2/releases/download/v2.25.0/bedtools-2.25.0.tar.gz
#RUN tar -zxvf bedtools-2.25.0.tar.gz 
#RUN cd bedtools2

# Groovy
RUN apt-get -y install groovy


# vcftools
RUN apt-get -y install vcftools
