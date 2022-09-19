from core.config import settings
import logging
from typing import Literal, Union
from slack_sdk.webhook import WebhookClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


webhook = WebhookClient(settings.SLACK_WEBHOOK_URL)


def send_message_to_slack(
        event: str, resource_type: str,  status: str, before: dict, after: dict, triggered_by: str):
    try:
        logger.info(f"sending message to slack channel")
        response = webhook.send(
            blocks=[
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "Change in Software Catalog :white_check_mark:"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": f"Triggered by {triggered_by}"
                        }
                    ]
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Change type*\n{event}"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Resource type*\n{resource_type}"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Status*\n{status}"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Before*\n```{before}```"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*After*\n```{after}```"
                    }
                },
                {
                    "type": "divider"
                }
            ]
        )

        logger.info('message sent')
        return response.status_code
    except Exception as err:
        logger.error(f"error sending message: {err}")
        return 500
