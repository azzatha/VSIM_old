FROM httpd

LABEL maintainer <azza.althagafi@kaust.edu.sa>

USER root

COPY . /usr/local/apache2/htdocs/

ENV DEBIAN_FRONTEND noninteractive

# Install all the requirements

# Python 3
RUN apt-get update  \
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

RUN conda config --add channels defaults 
#RUN conda config --add channels bioconda 
#RUN conda config --add channels conda-forge 
#RUN conda install -c bioconda vcfanno 

# bedtools http://bedtools.readthedocs.io/en/latest/content/installation.html
#RUN wget https://github.com/arq5x/bedtools2/releases/download/v2.25.0/bedtools-2.25.0.tar.gz
#RUN tar -zxvf bedtools-2.25.0.tar.gz 
#RUN cd bedtools2
#RUN make

# Groovy
#RUN sudo apt-get install groovy

# vcftools
#RUN sudo apt-get install vcftools
