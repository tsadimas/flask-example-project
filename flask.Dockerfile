FROM python:3.6.15-slim-bullseye

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Change working directory
WORKDIR /app
RUN apt update && apt install -y gcc default-libmysqlclient-dev

# COPY requirements.txt
COPY ./requirements.txt .

#install dependencies
RUN pip install -r requirements.txt

# COPY app files
COPY ./app .

CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:5000"]