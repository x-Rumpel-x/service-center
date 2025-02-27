FROM python:3.13

WORKDIR /app

RUN apt-get update && \
    apt-get install -y locales && \
    echo "ru_RU.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen ru_RU.UTF-8 && \
    update-locale LANG=ru_RU.UTF-8


ENV LANG=ru_RU.UTF-8 \
    LANGUAGE=ru_RU:ru \
    LC_ALL=ru_RU.UTF-8

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV FLASK_APP=run.py
ENV FLASK_ENV=production

EXPOSE 5002

CMD ["gunicorn", "--reload", "-w", "4", "-b", "0.0.0.0:5002", "run:app"]