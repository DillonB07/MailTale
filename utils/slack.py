from dotenv import load_dotenv
from slack_bolt import App
import os

from commands.subscribe import handle_subscribe
from commands.subscription import handle_subscription
from events.subscribe import handle_subscribe_address
from events.toggle_subscription import handle_toggle_subscription
from events.cancel_subscription import handle_cancel_subscription
from events.update_address import handle_update_address
from events.update_delivery_note import handle_update_delivery_note
from modals.manage_address import get_modal as get_manage_address_modal
from modals.update_address import get_modal as get_update_address_modal
from modals.update_delivery_note import get_modal as get_update_delivery_note_modal
from modals.manage_status import get_modal as get_manage_status_modal
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
@app.command("/dev-subscribe")
def subscribe_command(ack, respond, body, client):
    handle_subscribe(ack, respond, body, client)


@app.command("/subscription")
@app.command("/dev-subscription")
def subscription_command(ack, respond, body, client):
    handle_subscription(ack, respond, body, client)


@app.view("subscribe_address")
def subscribe_address(ack, body, client):
    ack()
    handle_subscribe_address(body, client)


@app.view("update_address")
def update_address_view(ack, body, client):
    ack()
    handle_update_address(body, client)


@app.view("update_delivery_note")
def update_delivery_note_view(ack, body, client):
    ack()
    handle_update_delivery_note(body, client)


@app.action("manage-address")
def manage_address(ack, body, client):
    ack()
    view = get_manage_address_modal(body["user"]["id"])
    client.views_push(view=view, trigger_id=body["trigger_id"])


@app.action("update-address")
def update_address(ack, body, client):
    ack()
    view = get_update_address_modal(body["user"]["id"])
    client.views_push(view=view, trigger_id=body["trigger_id"])

@app.action("update-delivery-notes")
def update_delivery_notes(ack, body, client):
    ack()
    view = get_update_delivery_note_modal(body["user"]["id"])
    client.views_push(view=view, trigger_id=body["trigger_id"])

@app.action("manage-status")
def manage_status(ack, body, client):
    ack()
    
    view = get_manage_status_modal(body["user"]["id"])
    client.views_push(view=view, trigger_id=body["trigger_id"])
    
    
@app.action("toggle-subscription")
def toggle_subscription(ack, body, client):
    ack()
    
    handle_toggle_subscription(body, client)
    
    
@app.action("cancel-subscription")
def cancel_subscription(ack, body, client):
    ack()
    handle_cancel_subscription(body, client)
