import logging
from fastapi import APIRouter, Depends
from datetime import datetime

from actions import send_message
from api.deps import verify_webhook
from core.config import settings
from schemas.webhook import Webhook

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/slack", dependencies=[Depends(verify_webhook)])
async def handle_changelog_webhook(webhook: Webhook):
    logger.info(f"Webhook body: {webhook}")
    event = webhook.action
    if event != "UPDATE":
        # Not a healthStatus update event
        return {"status": 200}
    entity = webhook.context.entity
    before = webhook.diff.before.properties["healthStatus"]
    after = webhook.diff.after.properties["healthStatus"]
    if before == after:
        # No change in healthStatus
        return {"status": 200}
    triggered_by = webhook.trigger.by.userId
    response = send_message.send_message_to_slack(before, after, entity, triggered_by)
    return {"status": response}
