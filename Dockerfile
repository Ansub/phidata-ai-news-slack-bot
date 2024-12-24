FROM python:3.9-slim-bullseye

# Install necessary packages (cron, git, etc.)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    cron \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Create necessary directories and files
RUN mkdir -p /app/src && \
    touch /var/log/cron.log

# Copy all project files into the container
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Export all environment variables to a file
RUN printenv | grep -v "no_proxy" >> /etc/environment

# Add the cron job
RUN echo "*/2 * * * * . /etc/environment && /usr/local/bin/python3 /app/src/slack_news_bot.py >> /var/log/cron.log 2>&1" > /etc/cron.d/news-bot-cron && \
    chmod 0644 /etc/cron.d/news-bot-cron && \
    crontab /etc/cron.d/news-bot-cron

# Start the cron service in the foreground
CMD ["cron", "-f"]
