FROM python:3.11-slim

WORKDIR /app

COPY controller.py .

RUN pip install kopf kubernetes jinja2

CMD ["kopf", "run", "--standalone", "--all-namespaces", "/app/controller.py"]