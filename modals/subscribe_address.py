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
                "block_id": "address",
                "element": {
                    "type": "plain_text_input",
                    "multiline": True,
                    "action_id": "address",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "7 Orpheus Avenue\nLittle Stoke\nBristol\nBS34 6JE",
                    },
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
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": country,
                                "emoji": True,
                            },
                            "value": country,
                        }
                        for country in COUNTRIES
                    ],
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
