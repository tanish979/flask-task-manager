FROM python:3.9
WORKDIR /app


RUN apt-get update && apt-get install -y libpq-dev gcc


COPY . .


RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt  # No need for virtualenv activation!


EXPOSE 5000


CMD ["python", "run.py"]
