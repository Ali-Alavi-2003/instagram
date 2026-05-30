# FROM python:3.12-slim
FROM docker.arvancloud.ir/python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --index-url https://package-mirror.liara.ir/repository/pypi/simple/ -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
