# Phidata AI News Slack Bot

A Docker-containerized bot that runs daily searches for tech updates using GPT-4o, DuckDuckGo and Phidata.

## Prerequisites

- direnv (`brew install direnv` on macOS)
- Docker
- Python 3.9+

## Setup

1. Clone the repository
2. Copy `.envrc.example` to `.envrc` and add your `OPENAI_API_KEY` and `SLACK_TOKEN`
3. Allow direnv:
   ```bash
   direnv allow
   ```
