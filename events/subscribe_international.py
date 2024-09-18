from modals.subscribe_international import get_modal
from utils.airtable import airtable


def handle_subscribe_international(body, client):
    user_id = body["user"]["id"]

    view = body["view"]
    data = view["state"]["values"]
    can_pay = (
        True
        if data["payment"]["payment"]["selected_option"]["value"] == "yes"
        else False
    )

    updates = {"Shipping Costs": can_pay}
    airtable.update_user(user_id=user_id, **updates)

    client.chat_postMessage(
        channel=user_id, user=user_id, text="Thanks for subscribing to the newsletter!"
    )

    client.chat_postMessage(
        channel=os.environ.get("PUB_CHANNEL_ID"),
        text=f":blob_bounce: Somebody has subscribed to the newsletter from {country}!! :yay:"
    )
