from utils.airtable import airtable
from .constants import COUNTRIES

def get_modal(user_id):
    user = airtable.get_user(user_id)
    if not user: return

    user_data = user["fields"]
    address = user["fields"]["Address"]
    name = user_data.get("Name", "")
    address_line_1 = user_data.get("Address Line 1", "")
    address_line_2 = user_data.get("Address Line 2", "")
    city = user_data.get("City", "")
    county = user_data.get("County", "")
    postcode = user_data.get("Postcode", "")
    country = user_data.get("Country", "")

    return {
        "type": "modal",
        "callback_id": "update_address",
        "title": {"type": "plain_text", "text": "Manage Subscription", "emoji": True},
        "submit": {"type": "plain_text", "text": "Continue", "emoji": True},
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "blocks": [
            {
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Update Address:",
                "emoji": True
			}
		},
            {
                "type": "input",
                "block_id": "name",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "name",
                    "placeholder": {"type": "plain_text", "text": "Heidi Hakkuun"},
                    "initial_value": name
                },
                "label": {"type": "plain_text", "text": "Name", "emoji": True},
            },
            {
                "type": "input",
                "block_id": "address_line_1",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "address_line_1",
                    "placeholder": {"type": "plain_text", "text": "7 Orpheus Avenue"},
                    "initial_value": address_line_1
                },
                "label": {
                    "type": "plain_text",
                    "text": "Address Line 1",
                    "emoji": True,
                },
            },
            {
                "type": "input",
                "block_id": "address_line_2",
                "optional": True,
                "element": {
                    "type": "plain_text_input",
                    "action_id": "address_line_2",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Phone: +44-800-RAC-COON",
                    },
                    "initial_value": address_line_2
                },
                "label": {
                    "type": "plain_text",
                    "text": "Address Line 2",
                    "emoji": True,
                },
            },
            {
                "type": "input",
                "block_id": "city",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "city",
                    "placeholder": {"type": "plain_text", "text": "Little Stoke"},
                    "initial_value": city
                },
                "label": {"type": "plain_text", "text": "City", "emoji": True},
            },
            {
                "type": "input",
                "block_id": "county",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "county",
                    "placeholder": {"type": "plain_text", "text": "Bristol"},
                    "initial_value": county
                },
                "label": {"type": "plain_text", "text": "County", "emoji": True},
            },
            {
                "type": "input",
                "block_id": "postcode",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "postcode",
                    "placeholder": {"type": "plain_text", "text": "BS34 6JE"},
                    "initial_value": postcode
                },
                "label": {"type": "plain_text", "text": "Post Code", "emoji": True},
            },
            {
                "type": "input",
                "block_id": "country",
                "element": {
                    "type": "static_select",
                    "action_id": "country",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select an item",
                        "emoji": True,
                    },
                    "initial_option": {
                        "text": {
                            "type": "plain_text",
                            "text": country,
                            "emoji": True,
                        },
                        "value": country,
                    },
                    "options": [ {
                        "text": {
                            "type": "plain_text",
                            "text": country,
                            "emoji": True,
                        },
                        "value": country,
                        } for country in COUNTRIES
                    ]
                },
                "label": {"type": "plain_text", "text": "Country", "emoji": True},
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "_If your country isn't here, select `Other` and send <@U054VC2KM9P> a DM asking about it._",
                    }
                ],
            },
        ],
    }