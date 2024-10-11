from dotenv import load_dotenv
from modals.subscribe_international import get_modal
from utils.airtable import airtable
import os

load_dotenv()

def handle_subscribe_address(body, client):
    user_id = body["user"]["id"]

    view = body["view"]
    data = view["state"]["values"]

    name = data["name"]["name"]["value"]
    raw_address = data["address"]["address"]["value"]
    country = data["country"]["country"]["selected_option"]["value"]

    airtable.create_user(
        user_id=user_id,
        name=name,
        raw_address=raw_address,
        country=country,
    )

    # if country != "United Kingdom":
    #     view = get_modal(user_id)
    #     client.views_open(trigger_id=body["trigger_id"], view=view)
    #     return

    client.chat_postMessage(
        channel=user_id,
        user=user_id,
        text="Thanks for subscribing to the newsletter!",
    )

    client.chat_postMessage(
        channel=os.environ.get("PUB_CHANNEL_ID"),
        text=f":blob_bounce: Somebody has subscribed to the newsletter from {country}!! :yay:"
    )

    client.chat_postMessage(
        channel=os.environ.get("PRIV_CHANNEL_ID"),
        text=f":blob_bounce: <@{user_id}> just subscribed from {country}!"
    )
