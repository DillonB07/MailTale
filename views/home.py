from utils.env import env
from datetime import datetime

def generate_home_tab(body, user):
    print("Generating home view for user", user)
    user_id = user

    mail_reqs = env.airtable.get_mailer_mail(user_id)
    if not mail_reqs:
        mail_reqs = []
    mail_blocks = []

    for mail_req in mail_reqs:
        if mail_req["fields"].get("Status", "") != "Sent":
            recipient = env.airtable.get_user(
                airtable_id=mail_req["fields"].get("Recipient", "")[0]
            )
            if not recipient:
                recipient = {"fields": {"Slack ID": "U07T57U1LP5"}}
            mail_blocks.append(
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": f"Sending to *<@{recipient['fields'].get('Slack ID')}>*",
                        }
                    ],
                }
            )
            mailable = env.airtable.get_mailable(mail_req["fields"].get("Type", "")[0])
            if not mailable:
                mailable = {
                    "fields": {
                        "Name": "404 Not Found",
                        "Description": "The requested mailable could not be found.",
                        "Link": "https://google.com/teapot",
                    }
                }
            timestamp_str = mail_req['fields'].get('Created', '2024-01-01T00:00:00.000Z')
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ")
            unix_timestamp = int(timestamp.timestamp())
            formatted_slack_ts = f"<!date^{unix_timestamp}^{{date_num}} at {{time_secs}}|{timestamp_str}>"
            mail_blocks.append(
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*{mailable['fields'].get('Name')}*\nType: *{'Domestic' if mail_req['fields'].get('Domestic', 0) == 1 else 'International'}*\nCountry: *{mail_req['fields'].get('Country')}*\nPending since: *{formatted_slack_ts}*",
                    },
                    "accessory": {
                        "type": "image",
                        "image_url": "https://api.slack.com/img/blocks/bkb_template_images/plane.png",
                        "alt_text": "plane",
                    },
                }
            )
            mail_blocks.append(
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": f'<https://airtable.com/{env.airtable_base_id}/{env.airtable_mail_requests_table_id}/{mail_req["id"]}|View on Airtable>',
                        }
                    ],
                }
            )
            mail_blocks.append(
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": (
                                    "Mark Sent"
                                    if mail_req["fields"].get("Status", "")
                                    == "Prepared"
                                    else "Ready to Send"
                                ),
                                "emoji": True,
                            },
                            "style": "primary",
                            "value": (
                                "mark-sent"
                                if mail_req["fields"].get("Status", "") == "Prepared"
                                else "mark-ready-to-send"
                            ),
                        },
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "View Details",
                                "emoji": True,
                            },
                            "value": "details",
                        },
                    ],
                }
            )
            mail_blocks.append({"type": "divider"})

    return {
        "type": "home",
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Mail Management",
                    "emoji": True,
                },
            },
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f":tw_wave: Hi <@{user_id}>"},
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "See Past Mail",
                        "emoji": True,
                    },
                    "value": "app_settings",
                },
            },
            {"type": "divider"},
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*My Stats*\n:tw_incoming_envelope: Total Sent · *150*\n:tw_house: Domestically Sent · *50*\n:tw_globe_with_meridians: Internationally Sent · *100*",
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Global Stats*\n:tw_incoming_envelope: Total Sent · *300*\n:tw_house: Domestically Sent · *100* \n:tw_globe_with_meridians: Internationally Sent · *200*",
                    },
                ],
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://api.slack.com/img/blocks/bkb_template_images/placeholder.png",
                        "alt_text": "placeholder",
                    }
                ],
            },
            {"type": "divider"},
            {"type": "section", "text": {"type": "mrkdwn", "text": "*Mail to Send*"}},
        ]
        + mail_blocks,
    }
