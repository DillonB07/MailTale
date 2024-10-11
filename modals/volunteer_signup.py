def get_modal(user_id):
    return {
        "type": "modal",
        "callback_id": "volunteer_signup",
        "title": {"type": "plain_text", "text": "Volunteer!", "emoji": True},
        "submit": {"type": "plain_text", "text": "Offer!", "emoji": True},
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"Hey <@{user_id}>, thanks for the offer to volunteer! Filling out this form does _not_ mean that you'll be helping, it's just to let me know that you're interested!",
                },
            },
            {"type": "divider"},
            {
                "type": "input",
                "block_id": "courier",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "courier",
                    "placeholder": {"type": "plain_text", "text": "Royal Mail"},
                },
                "label": {"type": "plain_text", "text": "What is the name of your local mail service? (please include capitals)", "emoji": True},
            },
            {
                "type": "input",
                "block_id": "domestic_price",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "domestic_price",
                    "placeholder": {"type": "plain_text", "text": "0.85"},
                },
                "label": {"type": "plain_text", "text": "What is the price of domestic shipping of 1 standard/small letter?", "emoji": True},
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "_Use your local currency and only put a number. Please include all applicable tax in the cost._",
                    }
                ],
            },
            {
                "type": "input",
                "block_id": "international_price",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "international_price",
                    "placeholder": {"type": "plain_text", "text": "2.80"},
                },
                "label": {"type": "plain_text", "text": "What is the price of international shipping of 1 standard/small letter?", "emoji": True},
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "_Use your local currency and only put a number. Please include all applicable tax in the cost._",
                    }
                ],
            },
            {
                "type": "input",
                "block_id": "currency",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "currency",
                    "placeholder": {"type": "plain_text", "text": "GBP"},
                },
                "label": {"type": "plain_text", "text": "What is your local currency?", "emoji": True},
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "_Please use the 3 digit currency code._",
                    }
                ],
            },
        ],
    }
