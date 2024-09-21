from utils.airtable import airtable
from .constants import COUNTRIES

def get_modal(user_id):
    user = airtable.get_user(user_id)
    if not user: return

    user_data = user["fields"]
    name = user_data.get("Name", "")
    raw_address = user_data.get("Raw Address", "")
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
            },{
                "type": "input",
                "block_id": "address",
                "element": {
                    "type": "plain_text_input",
                    "multiline": True,
                    "action_id": "address",
                    "initial_value": raw_address,
                },
                "label": {"type": "plain_text", "text": "Address", "emoji": True},
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