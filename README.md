# Mail Tale

Mail Tale is the Slack bot to manage subscriptions for my Hack Club community newsletter!

## Setup

### Create a Slack App

1. Go to the [Slack API](https://api.slack.com/apps) and create a new app
2. Use the following manifest:
```json
{
    "display_information": {
        "name": "Mail Tale",
        "description": "The tale of your mail is so beautiful",
        "background_color": "#702eb3"
    },
    "features": {
        "bot_user": {
            "display_name": "Mail Tale",
            "always_online": false
        },
        "slash_commands": [
            {
                "command": "/subscribe",
                "url": "URL",
                "description": "Subscribe to the #community-newsletter",
                "should_escape": false
            },
            {
                "command": "/subscription",
                "url": "URL",
                "description": "Manage your #community-newsletter subscription",
                "should_escape": false
            }
        ]
    },
    "oauth_config": {
        "scopes": {
            "bot": [
                "commands",
                "chat:write"
            ]
        }
    },
    "settings": {
        "event_subscriptions": {
            "request_url": "URL",
            "bot_events": [
                "app_home_opened"
            ]
        },
        "interactivity": {
            "is_enabled": true,
            "request_url": "URL"
        },
        "org_deploy_enabled": false,
        "socket_mode_enabled": false,
        "token_rotation_enabled": false
    }
}
```
3. Install the app to your workspace
4. Copy the bot token and signing secret

### Running the App

1. Clone the repository
2. Create a venv with `python3.12 -m venv .venv`
3. Activate the venv with `source .venv/bin/activate`
4. Install dependencies with `python3.12 -m pip install -r requirements.txt`
5. Create a `.env` file with the following variables:
   - `SLACK_BOT_TOKEN`: The Slack bot token
   - `SLACK_SIGNING_SECRET`: The Slack signing secret
   - `PUB_CHANNEL_ID`: The public channel to log to
   - `PRIV_CHANNEL_ID`: The private channel to log to (specifies users)
   - `PRIV_PRIV_CHANNEL_ID`: The bts channel to log to (for volunteers)
   - `AIRTABLE_TOKEN`: The Airtable API token with access to the base. Needs permissions to read and write.
   - `AIRTABLE_BASE_ID`: The Airtable base ID - get this from the URL
   - `AIRTABLE_PEOPLE_TABLE_ID`: The table ID of the People table - get this from the URL
   - `AIRTABLE_MAIL_REQUESTS_TABLE_ID`: The table ID of the Mail Requests table - get this from the URL
   - `AIRTABLE_MAIlABLES_TABLE_ID`: The table ID of the Mailables table - get this from the URL

6. Run the bot with `python3.12 app.py`
