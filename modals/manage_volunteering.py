from utils.env import env


def get_modal(user_id):
    user = env.airtable.get_user(slack_id=user_id)
    if not user:
        return
    is_volunteer = user["fields"].get("Wants to Mail", False)
    is_approved = user["fields"].get("Allowed to Mail", False)

    if is_volunteer and not is_approved:
        return {
            "type": "modal",
            "title": {
                "type": "plain_text",
                "text": "Manage Subscription",
                "emoji": True,
            },
            "close": {"type": "plain_text", "text": "Close"},
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "Manage Volunteering",
                        "emoji": True,
                    },
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": (
                            f"*Thanks for registering your interest to volunteer <@{user_id}> :hugg:*"
                            if is_volunteer
                            else "*You haven't registered to volunteer yet :roo-sad:*"
                        ),  # actually this should never happen, but just in case
                    },
                },
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": "Just a reminder, registering to volunteer doesn't mean that you'll be chosen. There are a lot of merits to keeping a small team, even more so with a project like this. The more people there are in more different places, the more complex managing this becomes with different prices, currencies, tax as well as all the normal complexities of managing a team.",
                        "emoji": True,
                    },
                },
                {
                    "type": "actions",
                    "block_id": "update-shipping-costs",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Update Shipping Costs",
                                "emoji": True,
                            },
                            "value": "update-shipping-costs",
                            "action_id": "update-shipping-costs",
                        }
                    ],
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "plain_text",
                            "text": "If you've moved or shipping costs from your location have changed, you can update them here!",
                            "emoji": True,
                        }
                    ],
                },
                {
                    "type": "actions",
                    "block_id": "remove-volunteer",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Unregister Interest",
                                "emoji": True,
                            },
                            "value": "remove-volunteer",
                            "action_id": "remove-volunteer",
                            "style": "danger",
                        }
                    ],
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "plain_text",
                            "text": "If you don't want to volunteer anymore for various reasons this will remove you from the list.",
                            "emoji": True,
                        }
                    ],
                },
            ],
        }

    if is_approved:
        mail = env.airtable.get_mailer_mail(user["id"])
        if not mail:
            mail = []
        sent = len([m for m in mail if m.get("Status") == "Mailed"])
        to_send = len([m for m in mail if m.get("Status") != "Mailed"])

        return {
            "type": "modal",
            "title": {
                "type": "plain_text",
                "text": "Manage Subscription",
                "emoji": True,
            },
            "close": {"type": "plain_text", "text": "Close"},
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "Manage Volunteering",
                        "emoji": True,
                    },
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Thanks for being a team member <@{user_id}>!*",
                    },
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "I'm sure you've been given the rundown on how this works. If you've got any questions, message <@U054VC2KM9P>!",
                    },
                },
                {"type": "divider"},
                {
                    "type": "rich_text",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Stats",
                                    "style": {"bold": True},
                                }
                            ],
                        },
                        {
                            "type": "rich_text_list",
                            "style": "bullet",
                            "elements": [
                                {
                                    "type": "rich_text_section",
                                    "elements": [
                                        {
                                            "type": "text",
                                            "text": "Mail to be sent: ",
                                            "style": {"bold": True},
                                        },
                                        {"type": "text", "text": str(to_send)},
                                    ],
                                },
                                {
                                    "type": "rich_text_section",
                                    "elements": [
                                        {
                                            "type": "text",
                                            "text": "Mail sent: ",
                                            "style": {"bold": True},
                                        },
                                        {"type": "text", "text": str(sent)},
                                    ],
                                },
                            ],
                        },
                    ],
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "View Assigned Mail",
                                "emoji": True,
                            },
                            "value": "view-assigned-mail",
                            "url": "https://hackclub.slack.com/archives/D07MHE2LS67",
                            "action_id": "view-assigned-mail",
                            "style": "primary",
                        }
                    ],
                },
                {"type": "divider"},
                {
                    "type": "actions",
                    "block_id": "update-shipping-costs",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Update Shipping Costs",
                                "emoji": True,
                            },
                            "value": "update-shipping-costs",
                            "action_id": "update-shipping-costs",
                        }
                    ],
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "plain_text",
                            "text": "If you've moved or shipping costs from your location have changed, please update them!",
                            "emoji": True,
                        }
                    ],
                },
            ],
        }
