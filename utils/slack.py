from dotenv import load_dotenv
from slack_bolt import App
import os

from commands.subscribe import handle_subscribe
from commands.subscription import handle_subscription
from events.subscribe_address import handle_subscribe_address
from events.subscribe_international import handle_subscribe_international
from views.home import generate_home_tab

load_dotenv()

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)


@app.event("app_home_opened")
def update_home_tab(client, event, logger):
    generate_home_tab(client, event["user"])


@app.command("/subscribe")
def subscribe_command(ack, respond, body, client):
    handle_subscribe(ack, respond, body, client)


@app.command("/subscription")
def subscription_command(ack, respond, body):
    handle_subscription(ack, respond, body)


@app.view("subscribe_address")
def subscribe_address(ack, body, client):
    ack()
    handle_subscribe_address(body, client)


@app.view("subscribe_intl")
def subscribe_intl(ack, body, client):
    ack()
    handle_subscribe_international(body, client)
