FROM python:3.9-slim

# Install cron and required packages
RUN apt-get update && apt-get -y install cron

# Set working directory
WORKDIR /app

# Create src directory
RUN mkdir -p /app/src

# Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Add crontab file
RUN echo "0 9 * * * . /app/.envrc && python /app/src/slack_news_bot.py >> /var/log/cron.log 2>&1" > /etc/cron.d/news-bot-cron
RUN chmod 0644 /etc/cron.d/news-bot-cron

# Apply cron job
RUN crontab /etc/cron.d/news-bot-cron

# Create log file
RUN touch /var/log/cron.log

# Run cron in foreground
CMD ["cron", "-f"]