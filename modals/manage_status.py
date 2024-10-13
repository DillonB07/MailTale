from utils.airtable import airtable


def get_modal(user_id):
    user = airtable.get_user(user_id)
    if not user:
        return
    paused = user["fields"].get("Paused", False)
    return {
        "title": {"type": "plain_text", "text": "Manage Subscription", "emoji": True},
        "type": "modal",
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "blocks": [
            {
                "type": "header",
                "text": {"type": "plain_text", "text": "Manage Status", "emoji": True},
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (
                        "Currently you are receiving mail each month! :roo-yay:"
                        if not paused
                        else "You are not currently receiving mail each month. :roo-sad:"
                    ),
                },
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": (
                                "Pause Subscription"
                                if not paused
                                else "Resume Subscription"
                            ),
                            "emoji": True,
                        },
                        "confirm": {
                            "text": {
                                "type": "plain_text",
                                "text": f"Are you sure you want to {'pause' if not paused else 'resume'} your subscription?",
                            }
                        },
                        "value": "toggle-subscription",
                        "action_id": "toggle-subscription",
                    }
                ],
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "plain_text",
                        "text": "Pausing your subscription will remove you from the mail lists until you unpause it. Your data will still be kept.",
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
                            "text": "Cancel Subscription",
                            "emoji": True,
                        },
                        "style": "danger",
                        "confirm": {
                            "text": {
                                "type": "plain_text",
                                "text": "Are you sure you want to cancel your   subscription?",
                            }
                        },
                        "value": "cancel-subscription",
                        "action_id": "cancel-subscription",
                    }
                ],
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "plain_text",
                        "text": "Cancelling your subscription will remove you from the mail lists and delete your entry in the database. This cannot be undone, but you can resubscribe later.",
                        "emoji": True,
                    }
                ],
            },
        ],
    }
