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
    address_line_1 = data["address_line_1"]["address_line_1"]["value"]
    address_line_2 = data["address_line_2"]["address_line_2"].get("value", "")
    city = data["city"]["city"]["value"]
    county = data["county"]["county"]["value"]
    postcode = data["postcode"]["postcode"]["value"]
    country = data["country"]["country"]["selected_option"]["value"]

    airtable.create_user(
        user_id=user_id,
        name=name,
        address_line_1=address_line_1,
        address_line_2=address_line_2,
        city=city,
        county=county,
        postcode=postcode,
        country=country,
    )

    if country != "United Kingdom":
        view = get_modal(user_id)
        client.views_open(trigger_id=body["trigger_id"], view=view)
        return

    client.chat_postMessage(
        channel=user_id,
        user=user_id,
        text="Thanks for subscribing to the newsletter!",
    )
    client.chat_postMessage(
        channel=os.environ.get("PUB_CHANNEL_ID")
        text=":blob_bounce: Somebody has subscribed to the newsletter from {country}!! :yay:"
    )
