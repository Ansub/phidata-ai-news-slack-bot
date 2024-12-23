import os
import json
from typing import Optional, Dict, Any
from phi.tools.toolkit import Toolkit
from phi.utils.log import logger
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class CustomSlackTools(Toolkit):
    def __init__(
        self,
        send_message: bool = True,
        list_channels: bool = True,
        get_channel_history: bool = True,
    ):
        super().__init__(name="slack")
        self.token: Optional[str] = os.getenv("SLACK_TOKEN")
        if self.token is None or self.token == "":
            raise ValueError("SLACK_TOKEN is not set")
        self.client = WebClient(token=self.token)
        if send_message:
            self.register(self.send_message)
        if list_channels:
            self.register(self.list_channels)
        if get_channel_history:
            self.register(self.get_channel_history)

    def send_message(self, channel: str, text: str, thread_ts: Optional[str] = None) -> str:
        """
        Send a message to a Slack channel without unfurling links.
        
        Args:
            channel (str): Channel name or ID
            text (str): Message text
            thread_ts (str, optional): Thread timestamp to reply to
        """
        try:
            params: Dict[str, Any] = {
                "channel": channel,
                "text": text,
                "unfurl_links": False,
                "unfurl_media": False
            }
            
            if thread_ts:
                params["thread_ts"] = thread_ts
                
            response = self.client.chat_postMessage(**params)
            return json.dumps(response.data)
        except SlackApiError as e:
            logger.error(f"Error sending message: {e}")
            return json.dumps({"error": str(e)})

    def list_channels(self) -> str:
        """
        List all channels in the Slack workspace.
        """
        try:
            response = self.client.conversations_list()
            channels = [{"id": channel["id"], "name": channel["name"]} for channel in response["channels"]]
            return json.dumps(channels)
        except SlackApiError as e:
            logger.error(f"Error listing channels: {e}")
            return json.dumps({"error": str(e)})

    def get_channel_history(self, channel: str, limit: int = 100) -> str:
        """
        Get the message history of a Slack channel.
        
        Args:
            channel (str): Channel ID
            limit (int): Maximum number of messages to fetch
        """
        try:
            response = self.client.conversations_history(channel=channel, limit=limit)
            messages = [{"text": msg["text"], "user": msg["user"], "ts": msg["ts"]} for msg in response["messages"]]
            return json.dumps(messages)
        except SlackApiError as e:
            logger.error(f"Error getting channel history: {e}")
            return json.dumps({"error": str(e)})

# Initialize the tools
def get_slack_tools():
    return CustomSlackTools()