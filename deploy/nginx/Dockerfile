FROM nginx:stable-alpine

RUN apk add --no-cache gettext && \
    adduser -D -u 1000 -g 'nginx' nginx && \
    chown -R nginx:nginx /var/cache/nginx && \
    chown -R nginx:nginx /var/log/nginx && \
    chmod -R 755 /var/log/nginx

COPY ./nginx.conf.template /tmp/nginx.conf.template

USER nginx

CMD ["sh", "-c", "envsubst < /tmp/nginx.conf.template > /etc/nginx/nginx.conf && nginx -g 'daemon off;'"]
