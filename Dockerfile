FROM alpine
MAINTAINER Ponnusamy <agoldgod@gmail.com>

RUN apk add --no-cache bash py2-pip \
	&& pip2 install --upgrade pip \
	&& pip2 install flask freeze 
RUN mkdir -p /opt/output
VOLUME ["/app/output"]
WORKDIR /app
ADD app.py /app/app.py 
ADD templates /app/templates
EXPOSE 8000
CMD [ "python", "./app.py" ]