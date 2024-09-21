from utils.airtable import airtable

def handle_update_address(body, client):
    user_id = body["user"]["id"]

    view = body["view"]
    data = view["state"]["values"]

    name = data["name"]["name"]["value"]
    raw_address = data["address"]["address"]["value"]
    country = data["country"]["country"]["selected_option"]["value"]

    updates = {
        "Name": name,
        "Raw Address": raw_address,
        "Country": country,
    }
    airtable.update_user(
        user_id=user_id,
        **updates
    )

    client.chat_postMessage(
        channel=user_id,
        user=user_id,
        text="Your address has been updated!",
    )
