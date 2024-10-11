from utils.airtable import airtable

def handle_volunteer_signup(body, client):
    user_id = body["user"]["id"]
    
    view = body["view"]
    data = view["state"]["values"]

    courier = data["courier"]["courier"]["value"]
    domestic_price = data["domestic_price"]["domestic_price"]["value"]
    international_price = data["international_price"]["international_price"]["value"]
    currency = data["currency"]["currency"]["value"]

    updates = {
        "Local Courier": courier,
        "Domestic Shipping Cost": float(domestic_price),
        "International Shipping Cost": float(international_price),
        "Local Currency": currency,
        "Wants to Mail": True,
    }

    airtable.update_user(
        user_id=user_id,
        **updates
    )

    client.chat_postMessage(
        channel=user_id,
        user=user_id,
        text="Thanks for signing up to volunteer! If I need the help, I'll be in touch!",
    )
