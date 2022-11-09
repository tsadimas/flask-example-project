FROM python:3.10-slim-bullseye

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install libmariadb-dev-compat gcc -y

WORKDIR /data

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./app .

CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:5000"]
#CMD ["sleep", "5000"]