# Use ARM-compatible base image
FROM arm64v8/python:3.9-slim-bullseye

# Install cron and required packages with minimal layer size
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    cron \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Create src directory and log file
RUN mkdir -p /app/src && \
    touch /var/log/cron.log

# Copy requirements first to leverage Docker cache
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Add crontab file and set permissions
RUN echo "0 9 * * * . /app/.envrc && python /app/src/slack_news_bot.py >> /var/log/cron.log 2>&1" > /etc/cron.d/news-bot-cron && \
    chmod 0644 /etc/cron.d/news-bot-cron && \
    crontab /etc/cron.d/news-bot-cron

# Run cron in foreground
CMD ["cron", "-f"]