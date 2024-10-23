from utils.env import env


def handle_update_delivery_note(body, client):
    view = body["view"]
    user_id = body["user"]["id"]
    user = env.airtable.get_user(slack_id=user_id)
    if not user:
        return

    new_note = view["state"]["values"]["delivery-note"]["delivery-note"]["value"]

    env.airtable.update_user(user_id, **{"Delivery Notes": new_note})

    client.chat_postMessage(
        channel=user_id, text="Your delivery notes have been updated"
    )
