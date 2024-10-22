from modals.manage_subscription import get_modal
from utils.env import env


def handle_subscription(ack, respond, body, client):
    ack()

    user_id = body.get("user_id")
    user = env.airtable.get_user(user_id)

    if not user:
        respond(
            "You aren't subscribed to the newsletter yet! Run /subscribe to get started."
        )
        return

    view = get_modal(user_id)
    client.views_open(trigger_id=body["trigger_id"], view=view)
