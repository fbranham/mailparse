FROM alpine
MAINTAINER Christian Gatzlaff <cgatzlaff@gmail.com>

# basic flask environment
RUN apk add --no-cache bash git nginx uwsgi uwsgi-python py3-pip \
	&& pip3 install --upgrade pip \
	&& pip3 install flask

# application folder
ENV APP_DIR /app

# copy config files into filesystem
COPY nginx.conf /etc/nginx/nginx.conf
COPY app.ini /app.ini
COPY entrypoint.sh /entrypoint.sh
COPY mailparse/ /app

# app dir
RUN mkdir -p ${APP_DIR} \
	&& chown -R nginx:nginx ${APP_DIR} \
	&& chmod 777 /run/ -R \
	&& chmod 777 /root/ -R


# expose web server port
# only http, for ssl use reverse proxy
EXPOSE 80




RUN chmod +x /entrypoint.sh

# execute start up script
ENTRYPOINT ["/entrypoint.sh"]