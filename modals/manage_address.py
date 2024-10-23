from utils.env import env


def get_modal(user_id):

    user = env.airtable.get_user(slack_id=user_id)
    if not user:
        return

    return {
        "type": "modal",
        "callback_id": "manage_address",
        "title": {"type": "plain_text", "text": "Manage Subscription", "emoji": True},
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "blocks": [
            {
                "type": "rich_text",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {"type": "text", "text": "Address", "style": {"bold": True}}
                        ],
                    },
                    {
                        "type": "rich_text_preformatted",
                        "elements": [
                            {"type": "text", "text": user["fields"]["Address"]}
                        ],
                    },
                ],
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "Mail will be sent to you with the address shown above. It will only be accessible by <@U054VC2KM9P> and Hack Clubbers assigned to send you mail.\nIf you've just updated your address, you will need to re-open this modal to see the changes.",
                    }
                ],
            },
            {
                "type": "actions",
                "block_id": "update-address",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Update Address",
                            "emoji": True,
                        },
                        "value": "update-address",
                        "action_id": "update-address",
                    }
                ],
            },
            {
                "type": "rich_text",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "text",
                                "text": "Delivery Notes",
                                "style": {"bold": True},
                            }
                        ],
                    },
                    {
                        "type": "rich_text_preformatted",
                        "elements": [
                            {
                                "type": "text",
                                "text": user["fields"].get(
                                    "Delivery Notes", "No notes specified"
                                ),
                            }
                        ],
                    },
                ],
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "plain_text",
                        "text": "These notes will be passed to the Hack Clubber mailing to you",
                        "emoji": True,
                    }
                ],
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Update Delivery Notes",
                            "emoji": True,
                        },
                        "value": "update-delivery-notes",
                        "action_id": "update-delivery-notes",
                    }
                ],
            },
        ],
    }
