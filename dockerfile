FROM python:3.11-slim

RUN mkdir /main

WORKDIR main

COPY requirements.txt /main
COPY . /main

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]