from utils.env import env


def get_modal(user_id, update=False):
    user = env.airtable.get_user(slack_id=user_id)
    if not user:
        return

    courier = user["fields"].get("Local Courier", "Royal Mail")
    domestic_price = str(user["fields"].get("Domestic Shipping Cost", "0.85"))
    international_price = str(user["fields"].get("International Shipping Cost", "2.80"))
    currency = user["fields"].get("Local Currency", "GBP")

    return {
        "type": "modal",
        "callback_id": "volunteer_signup",
        "title": {"type": "plain_text", "text": "Volunteer!", "emoji": True},
        "submit": {
            "type": "plain_text",
            "text": "Offer!" if not update else "Update",
            "emoji": True,
        },
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (
                        f"Hey <@{user_id}>, thanks for the offer to volunteer! Filling out this form does _not_ mean that you'll be helping, it's just to let me know that you're interested!"
                        if not update
                        else "Hey <@{user_id}>, please update the shipping information for your area below!"
                    ),
                },
            },
            {"type": "divider"},
            {
                "type": "input",
                "block_id": "courier",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "courier",
                    "initial_value": courier,
                },
                "label": {
                    "type": "plain_text",
                    "text": "What is the name of your local mail service? (please include capitals)",
                    "emoji": True,
                },
            },
            {
                "type": "input",
                "block_id": "domestic_price",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "domestic_price",
                    "initial_value": domestic_price,
                },
                "label": {
                    "type": "plain_text",
                    "text": "What is the price of domestic shipping of 1 standard/small letter?",
                    "emoji": True,
                },
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
                    "initial_value": international_price,
                },
                "label": {
                    "type": "plain_text",
                    "text": "What is the price of international shipping of 1 standard/small letter?",
                    "emoji": True,
                },
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
                    "initial_value": currency,
                },
                "label": {
                    "type": "plain_text",
                    "text": "What is your local currency?",
                    "emoji": True,
                },
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
