from .constants import COUNTRIES

def get_modal(user_id):
    return {
        "type": "modal",
        "callback_id": "subscribe_address",
        "title": {"type": "plain_text", "text": "Subscribe!", "emoji": True},
        "submit": {"type": "plain_text", "text": "Continue", "emoji": True},
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"Heya <@{user_id}>, I think that email is so boring now. Let's be honest, you don't enjoy reading your emails. So, why should you? I'll send you a physical letter each month!",
                },
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "_Just to be clear, I'm doing this of my own accord and this is not endorsed by HQ._",
                    }
                ],
            },
            {"type": "divider"},
            {
                "type": "input",
                "block_id": "name",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "name",
                    "placeholder": {"type": "plain_text", "text": "Heidi Hakkuun"},
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
