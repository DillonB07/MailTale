from slack_bolt import App

from commands.subscribe import handle_subscribe
from commands.subscription import handle_subscription
from events.subscribe import handle_subscribe_address
from events.toggle_subscription import handle_toggle_subscription
from events.cancel_subscription import handle_cancel_subscription
from events.update_address import handle_update_address
from events.update_delivery_note import handle_update_delivery_note
from events.volunteer_signup import handle_volunteer_signup
from events.remove_volunteer import handle_remove_volunteer
from modals.manage_address import get_modal as get_manage_address_modal
from modals.update_address import get_modal as get_update_address_modal
from modals.update_delivery_note import get_modal as get_update_delivery_note_modal
from modals.manage_status import get_modal as get_manage_status_modal
from modals.manage_volunteering import get_modal as get_manage_volunteering_modal
from modals.volunteer_info import get_modal as get_volunteer_info_modal
from modals.volunteer_signup import get_modal as get_volunteer_signup_modal
from utils.env import env
from views.home import generate_home_tab

app = App(
    token=env.slack_bot_token,
    signing_secret=env.slack_signing_secret,
)


@app.event("app_home_opened")
def update_home_tab(client, event, logger):
    view = generate_home_tab(client, event["user"])
    client.views_publish(user_id=event["user"], view=view)


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


@app.action("manage-volunteering")
def manage_volunteering(ack, body, client):
    ack()
    view = get_manage_volunteering_modal(body["user"]["id"])
    client.views_push(trigger_id=body["trigger_id"], view=view)


@app.action("volunteer-info")
def volunteer_info(ack, body, client):
    ack()
    view = get_volunteer_info_modal(body["user"]["id"])
    client.views_push(trigger_id=body["trigger_id"], view=view)


@app.view("volunteer_info")
def handle_view_submission_events(ack, body):
    view = get_volunteer_signup_modal(body["user"]["id"], update=False)
    ack(response_action="update", view=view)


@app.view("volunteer_signup")
def volunteer_signup(ack, body, client):
    ack()
    handle_volunteer_signup(body, client)


@app.action("update-shipping-costs")
def update_shipping_costs(ack, body, client):
    ack()
    view = get_volunteer_signup_modal(body["user"]["id"], update=True)
    client.views_push(trigger_id=body["trigger_id"], view=view)


@app.action("remove-volunteer")
def remove_volunteer(ack, body, client):
    ack()

    handle_remove_volunteer(body, client)
