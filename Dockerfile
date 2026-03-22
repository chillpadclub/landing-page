FROM nginx:alpine

RUN apk add --no-cache python3

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/chillpad.conf

COPY index.template.html /app/index.template.html

COPY logo_default.b64 /app/logo_default.b64

COPY entrypoint.py /app/entrypoint.py
RUN chmod +x /app/entrypoint.py

EXPOSE 80
CMD ["python3", "/app/entrypoint.py"]
