from dotenv import load_dotenv
from pyairtable import Api
import os

load_dotenv()


class AirtableManager:
    def __init__(self, api_key, base_id):
        api = Api(api_key)
        self.subscribers = api.table(base_id, "People")
        print("Connected to Airtable")

    def get_users(self):
        return self.subscribers.all()

    def get_user(self, user_id):
        user = self.subscribers.first(formula=f'{{Slack ID}} = "{user_id}"')
        return user

    def create_user(
        self,
        user_id,
        name,
        raw_address,
        country,
    ):
        print(f"Creating user with ID: {user_id}")
        self.subscribers.create(
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
        self.subscribers.update(user["id"], updates)
        
    def delete_user(self, user_id):
        user = self.get_user(user_id)
        if not user:
            return
        self.subscribers.delete(user["id"])


airtable = AirtableManager(
    api_key=os.environ.get("AIRTABLE_TOKEN"), base_id=os.environ.get("AIRTABLE_BASE_ID")
)
