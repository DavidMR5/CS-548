FROM python:3.11-slim

WORKDIR /app

COPY controller.py .

RUN pip install flask jsonpatch

EXPOSE 8000

CMD ["python", "controller.py"]