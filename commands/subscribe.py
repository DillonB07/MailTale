from utils.airtable import airtable
from modals.subscribe_address import get_modal


def handle_subscribe(ack, respond, body, client):
    ack()

    user_id = body.get("user_id")
    user = airtable.get_user(user_id)
    if user:
        respond(
            "You are already subscribed to the newsletter! Run /subscription to manage your subscription."
        )
        return

    view = get_modal(user_id)
    client.views_open(trigger_id=body["trigger_id"], view=view)
