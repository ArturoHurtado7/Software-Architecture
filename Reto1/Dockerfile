FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y gettext

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# export requirements.txt file
RUN pip freeze > requirements.txt

# Run application in port 8000
EXPOSE 8000
CMD uvicorn main:app --host 0.0.0.0 --port 8000 --workers 9
