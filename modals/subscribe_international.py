def get_modal(user_id):
    return {
        "callback_id": "subscribe_intl",
        "title": {"type": "plain_text", "text": "Subscribe - Int'l", "emoji": True},
        "submit": {"type": "plain_text", "text": "Submit", "emoji": True},
        "type": "modal",
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"I'm so glad you're interested <@{user_id}>!\n\n\n\nUnfortunately, international postage is expensive and costs 3x as much as domestic. I would love to ship you your newsletter, but you will need to pay for postage yourself.\n\n\nInternational postage costs £2.50 (approx 3.30USD). If you're willing to pay this much plus HCB tax per month, I'll gladly ship you a newsletter!\n\nIf not, that's ok, you can still be on the interested list and maybe I'll be able to ship you it, no promises though.",
                },
            },
            {
                "type": "input",
                "block_id": "payment",
                "element": {
                    "type": "radio_buttons",
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "I can pay for shipping",
                                "emoji": True,
                            },
                            "value": "yes",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "I cannot pay for shipping",
                                "emoji": True,
                            },
                            "value": "no",
                        },
                    ],
                    "action_id": "payment",
                },
                "label": {
                    "type": "plain_text",
                    "text": "Can you pay for shipping? (2.75 GBP / 3.60 USD)",
                    "emoji": True,
                },
            },
        ],
    }
