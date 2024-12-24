from datetime import datetime
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from tools import get_slack_tools

slack_tools = get_slack_tools()

slack_news_bot = Agent(
    name="Web Agent",
    model=OpenAIChat(id="gpt-4"),
    tools=[DuckDuckGo(), slack_tools],
    instructions=[
        "Only include news from the last 24 hours",
        "If no news is found from the last 24 hours, respond with: '*📰 AI News Update: {date}*\n\nNo major AI updates in the last 24 hours.'",
        "Verify the date in each article before including it",
        "Format: number. *Headline* (<URL|Read More>)",
        "Prioritize news from reliable tech sources",
        "Exclude any news older than 24 hours"
    ],
    show_tool_calls=True,
    markdown=True,
)

current_date = datetime.now().strftime("%Y-%m-%d")
message = f"""Search for AI news from the last 24 hours only and send to #tech-updates.

Search for these categories (ONLY from the last 24 hours):
- New AI model releases and announcements
- Multimodal AI developments
- AI agent systems
- Major AI company news (OpenAI, Anthropic, Google, DeepMind)

If no news from the last 24 hours is found, send:
*📰 AI News Update: {current_date}*

No major AI updates in the last 24 hours.

If news is found, format as:
*📰 AI News Update: {current_date}*

1. *Headline* (<URL|Read More>)

IMPORTANT: Only include news published in the last 24 hours. Verify dates before including."""

slack_news_bot.print_response(message, stream=True)