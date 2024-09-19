from utils.airtable import airtable
from modals.manage_address import get_modal

def handle_update_address(body, client):
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

    updates = {
        "Name": name,
        "Address Line 1": address_line_1,
        "Address Line 2": address_line_2,
        "City": city,
        "County": county,
        "Postcode": postcode,
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

    updated_view = get_modal(user_id)
    client.views_publish(
        view_id=view["id"],
        view=updated_view
    )