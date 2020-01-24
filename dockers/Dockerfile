FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash vi
COPY ./app /app
RUN pip install -r /app/req.txt
RUN ln -s /app/webapp.nginx.conf /etc/nginx/conf.d/webapp.conf

