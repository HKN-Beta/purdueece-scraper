FROM httpd:latest
MAINTAINER hknexec@purdue.edu
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install bs4
RUN pip3 install requests
COPY index.html /usr/local/apache2/htdocs/
COPY scrape.cgi /usr/local/apache2/htdocs/
RUN /bin/bash -c 'chmod +x /usr/local/apache2/htdocs/scrape.cgi'
COPY .htaccess /usr/local/apache2/htdocs/
COPY httpd.conf /usr/local/apache2/conf/
RUN /bin/bash -c 'mkdir /usr/local/apache2/htdocs/assets'
ADD assets /usr/local/apache2/htdocs/assets/
EXPOSE 80