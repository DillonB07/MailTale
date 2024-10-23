from dotenv import load_dotenv
from pyairtable import Api
import os

load_dotenv()


class AirtableManager:
    def __init__(
        self, api_key, base_id, people_table_id, mail_reqs_table_id, mailables_table_id
    ):
        api = Api(api_key)
        self.people = api.table(base_id, people_table_id)
        self.mail_requests = api.table(base_id, mail_reqs_table_id)
        self.mailables = api.table(base_id, mailables_table_id)
        print("Connected to Airtable")

    def get_users(self):
        return self.people.all()

    def get_user(self, slack_id: str | None = None, airtable_id: str | None = None):
        if slack_id:
            user = self.people.first(formula=f'{{Slack ID}} = "{slack_id}"')
        elif airtable_id:
            user = self.people.get(airtable_id)
        else:
            user = {}
        return user

    def create_user(
        self,
        user_id,
        name,
        raw_address,
        country,
    ):
        self.people.create(
            {
                "Slack ID": user_id,
                "Name": name,
                "Raw Address": raw_address,
                "Country": country,
            }
        )

    def update_user(self, user_id, **updates):
        user = self.get_user(slack_id=user_id)
        if not user:
            return
        self.people.update(user["id"], updates)

    def delete_user(self, user_id):
        user = self.get_user(slack_id=user_id)
        if not user:
            return
        self.people.delete(user["id"])

    def get_mailer_mail(self, mailer_id):
        mail = self.mail_requests.all(formula=f'{{Mailer}} = "{mailer_id}"')
        return mail

    def get_mailable(self, mailable_id):
        mailable = self.mailables.get(mailable_id)
        return mailable
