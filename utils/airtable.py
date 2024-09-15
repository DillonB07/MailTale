from dotenv import load_dotenv
from pyairtable import Api
import os

load_dotenv()


class AirtableManager:
    def __init__(self, api_key, base_id):
        api = Api(api_key)
        self.subscribers = api.table(base_id, "Subscribers")
        print("Connected to Airtable")

    def get_user(self, user_id):
        user = self.subscribers.first(formula=f'{{Slack ID}} = "{user_id}"')
        return user

    def create_user(
        self,
        user_id,
        name,
        address_line_1,
        address_line_2,
        city,
        county,
        postcode,
        country,
    ):
        print(f"Creating user with ID: {user_id}")
        self.subscribers.create(
            {
                "Slack ID": user_id,
                "Name": name,
                "Address Line 1": address_line_1,
                "Address Line 2": address_line_2,
                "City": city,
                "County": county,
                "Postcode": postcode,
                "Country": country,
            }
        )

    def update_user(self, user_id, **updates):
        user = self.get_user(user_id)
        if not user:
            return
        self.subscribers.update(user["id"], updates)


airtable = AirtableManager(
    api_key=os.environ.get("AIRTABLE_TOKEN"), base_id=os.environ.get("AIRTABLE_BASE_ID")
)
