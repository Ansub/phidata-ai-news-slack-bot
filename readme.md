# Phidata AI News Slack Bot

A Docker-containerized bot that runs daily at 5:55 PM IST to fetch and post AI news updates to Slack using GPT-4, DuckDuckGo, and Phidata.

## Features

- Automated daily AI news updates at 5:55 PM IST
- Containerized deployment using Docker
- Easy management through Portainer
- Automatic restarts and health monitoring
- Real-time logging

## Prerequisites

- Docker
- Portainer
- OpenAI API Key
- Slack Bot Token

## Local Development Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and add your credentials:
   ```env
   export OPENAI_API_KEY="your_key_here"
   export SLACK_TOKEN="your_token_here"
   ```
3. Run locally:
   ```bash
   python src/slack_news_bot.py
   ```

## Portainer Deployment

1. In Portainer:

   - Go to "Stacks" → Add stack
   - Name it (e.g., "slack-news-bot")
   - Copy the contents of `docker-compose.yml`

2. Set Environment Variables:

   - `OPENAI_API_KEY`: Your OpenAI API key
   - `SLACK_TOKEN`: Your Slack Bot token

3. Deploy the stack

The bot will automatically:

- Run every day at 5:55 PM IST
- Post updates to #tech-updates Slack channel
- Restart if there are any issues
- Log all activities

## Monitoring

View bot status and logs in Portainer:

1. Go to Containers
2. Select your bot container
3. Check the Logs tab

## Environment Variables

- `OPENAI_API_KEY`: OpenAI API key for GPT-4
- `SLACK_TOKEN`: Slack Bot User OAuth Token
