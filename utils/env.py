from .airtable import AirtableManager
from dotenv import load_dotenv
import os

load_dotenv()


class Environment:
    def __init__(self):
        self.slack_bot_token = os.environ.get("SLACK_BOT_TOKEN")
        self.slack_signing_secret = os.environ.get("SLACK_SIGNING_SECRET")
        self.slack_public_channel = os.environ.get("PUB_CHANNEL_ID")
        self.slack_mailroom_channel = os.environ.get("PRIV_CHANNEL_ID")
        self.slack_bts_channel = os.environ.get("PRIV_PRIV_CHANNEL_ID")
        self.airtable_api_key = os.environ.get("AIRTABLE_TOKEN")
        self.airtable_base_id = os.environ.get("AIRTABLE_BASE_ID")
        self.airtable_people_table_id = os.environ.get("AIRTABLE_PEOPLE_TABLE_ID")
        self.airtable_mail_requests_table_id = os.environ.get(
            "AIRTABLE_MAIL_REQUESTS_TABLE_ID"
        )
        self.airtable_mailables_table_id = os.environ.get("AIRTABLE_MAILABLES_TABLE_ID")

        self.port = int(os.environ.get("PORT", 3000))

        if not self.slack_bot_token:
            raise Exception("SLACK_BOT_TOKEN is not set")
        if not self.slack_signing_secret:
            raise Exception("SLACK_SIGNING_SECRET is not set")
        if not self.slack_public_channel:
            raise Exception("PUB_CHANNEL_ID is not set")
        if not self.slack_mailroom_channel:
            raise Exception("PRIV_CHANNEL_ID is not set")
        if not self.slack_bts_channel:
            raise Exception("PRIV_PRIV_CHANNEL_ID is not set")
        if not self.airtable_api_key:
            raise Exception("AIRTABLE_TOKEN is not set")
        if not self.airtable_base_id:
            raise Exception("AIRTABLE_BASE_ID is not set")
        if not self.airtable_people_table_id:
            raise Exception("AIRTABLE_PEOPLE_TABLE_ID is not set")
        if not self.airtable_mail_requests_table_id:
            raise Exception("AIRTABLE_MAIL_REQUESTS_TABLE_ID is not set")
        if not self.airtable_mailables_table_id:
            raise Exception("AIRTABLE_MAILABLES_TABLE_ID is not set")

        self.airtable = AirtableManager(
            api_key=self.airtable_api_key,
            base_id=self.airtable_base_id,
            people_table_id=self.airtable_people_table_id,
            mail_reqs_table_id=self.airtable_mail_requests_table_id,
            mailables_table_id=self.airtable_mailables_table_id,
        )


env = Environment()
