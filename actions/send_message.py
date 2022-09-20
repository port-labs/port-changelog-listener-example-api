from core.config import settings
import logging
from typing import Literal, Union
from slack_sdk.webhook import WebhookClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

webhook = WebhookClient(settings.SLACK_WEBHOOK_URL)

HEALTH_STATUS_DICT = {
    "Healthy": ":white_check_mark:",
    "Degraded": ":construction:",
    "Crashed": ":octagonal_sign:",
    "Restarting": ":arrows_counterclockwise:",
}


def send_message_to_slack(before: str, after: str, entity: str, triggered_by: str):
    try:
        logger.info(f"sending message to slack channel")
        response = webhook.send(
            blocks=[
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": f"Change in {entity} health status :construction:",
                    },
                },
                {"type": "divider"},
                {
                    "type": "context",
                    "elements": [{"type": "mrkdwn", "text": f"Triggered by {triggered_by}"}],
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Before*\n{before} {HEALTH_STATUS_DICT[before]}",
                    },
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Now*\n{after} {HEALTH_STATUS_DICT[after]}",
                    },
                },
                {"type": "divider"},
            ]
        )

        logger.info("message sent")
        return response.status_code
    except Exception as err:
        logger.error(f"error sending message: {err}")
        return 500
