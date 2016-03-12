from ubuntu:precise

maintainer dj

RUN apt-get -qy update --fix-missing
RUN apt-get install -qy curl

#---------- Latest Nginx (http2)
# Make a backup copy of your current sources.list file
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak
# Now copy the following repositories to the end of ` /etc/apt/sources.list`
RUN echo "deb http://nginx.org/packages/mainline/ubuntu/ trusty nginx" >> /etc/apt/sources.list
RUN echo "deb-src http://nginx.org/packages/mainline/ubuntu/ trusty nginx"  >> /etc/apt/sources.list
RUN curl http://nginx.org/keys/nginx_signing.key | apt-key add -
#----------

RUN apt-get -qy update
RUN apt-get install -qy git python python-dev python-setuptools libpq-dev nginx supervisor bc
RUN apt-get install -qy postgresql-client

# for Pillow pip installation
RUN apt-get install -qy libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev

# For GEODJANGO
RUN apt-get install -qy libgeos-dev

RUN easy_install pip
RUN pip install uwsgi

# install our code
ADD . /opt/Project/

# setup all the config files
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN mkdir -p /etc/nginx/sites-available/
RUN mkdir -p /etc/nginx/sites-enabled/
RUN rm -f /etc/nginx/conf.d/default
RUN ln -s /opt/Project/docker/django/nginx-app.conf /etc/nginx/sites-enabled/
RUN ln -s /opt/Project/docker/django/supervisor-app.conf /etc/supervisor/conf.d/
RUN rm -f /etc/nginx/nginx.conf
RUN ln -s /opt/Project/docker/django/nginx.conf /etc/nginx/;

# RUN pip install
RUN pip install -r /opt/Project/docker/django/requirements.txt

expose 80

CMD ["/opt/Project/docker/django/run.sh"]
