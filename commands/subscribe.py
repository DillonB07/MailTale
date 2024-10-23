from modals.subscribe_address import get_modal
from utils.env import env


def handle_subscribe(ack, respond, body, client):
    ack()

    user_id = body.get("user_id")
    user = env.airtable.get_user(slack_id=user_id)
    if user:
        respond(
            "You are already subscribed to the newsletter! Run /subscription to manage your subscription."
        )
        return

    view = get_modal(user_id)
    client.views_open(trigger_id=body["trigger_id"], view=view)
