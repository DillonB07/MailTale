from utils.env import env


def get_modal(user_id):
    user = env.airtable.get_user(slack_id=user_id)
    if not user:
        return
    paused = user["fields"].get("Paused", False)
    is_volunteer = user["fields"].get("Wants to Mail", False)

    return {
        "type": "modal",
        "callback_id": "manage_subscription",
        "title": {"type": "plain_text", "text": "Manage Subscription", "emoji": True},
        "close": {"type": "plain_text", "text": "Close", "emoji": True},
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": (
                        "Your newsletter subscription is :sparkles: active :sparkles: :roo-yay:"
                        if not paused
                        else "Your newsletter subscription is :no_entry_sign: paused :no_entry_sign: :roo-sad:"
                    ),
                    "emoji": True,
                },
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"Welcome to the mail management dashboard <@{user_id}>!\nPlease choose an option below.",
                },
            },
            {
                "type": "actions",
                "block_id": "manage-address",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Manage Address",
                            "emoji": True,
                        },
                        "value": "manage-address",
                        "action_id": "manage-address",
                    }
                ],
            },
            {
                "type": "actions",
                "block_id": "manage-status",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Manage Status",
                            "emoji": True,
                        },
                        "value": "manage-status",
                        "action_id": "manage-status",
                    }
                ],
            },
            (
                {
                    "type": "actions",
                    "block_id": "manage-volunteering",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Manage Volunteering",
                                "emoji": True,
                            },
                            "value": "manage-volunteering",
                            "action_id": "manage-volunteering",
                        }
                    ],
                }
                if is_volunteer
                else {
                    "type": "actions",
                    "block_id": "volunteer-info",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Sign up to volunteer",
                                "emoji": True,
                            },
                            "value": "volunteer-info",
                            "action_id": "volunteer-info",
                        }
                    ],
                }
            ),
        ],
    }
