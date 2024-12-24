# Use Python 3.11 as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY src/ src/

# Set the Python path to include src directory
ENV PYTHONPATH=/app

# Run the bot
CMD ["python", "src/slack_news_bot.py"]
