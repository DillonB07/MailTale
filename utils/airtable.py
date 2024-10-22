from dotenv import load_dotenv
from pyairtable import Api
import os

load_dotenv()


class AirtableManager:
    def __init__(self, api_key, base_id):
        api = Api(api_key)
        self.people = api.table(base_id, "People")
        self.mail_requests = api.table(base_id, "Mail Requests")
        self.mailables = api.table(base_id, "Mailables")
        print("Connected to Airtable")

    def get_users(self):
        return self.people.all()

    def get_user(self, user_id):
        user = self.people.first(formula=f'{{Slack ID}} = "{user_id}"')
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
        user = self.get_user(user_id)
        if not user:
            return
        self.people.update(user["id"], updates)

    def delete_user(self, user_id):
        user = self.get_user(user_id)
        if not user:
            return
        self.people.delete(user["id"])

    def get_mailer_mail(self, mailer_id):
        mail = self.mail_requests.first(formula=f'{{Mailer}} = "{mailer_id}"')
        return mail

