FROM python:3.9-slim-bullseye

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    cron \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN mkdir -p /app/src && \
    touch /var/log/cron.log

COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt

RUN echo "30 7 * * * . /app/.envrc && python /app/src/slack_news_bot.py >> /var/log/cron.log 2>&1" > /etc/cron.d/news-bot-cron && \
    chmod 0644 /etc/cron.d/news-bot-cron && \
    crontab /etc/cron.d/news-bot-cron

CMD ["cron", "-f"]