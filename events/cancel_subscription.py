from utils.airtable import airtable

def handle_cancel_subscription(body, client):
    user_id = body["user"]["id"]
    airtable.delete_user(user_id)
    
    client.chat_postMessage(
        channel=user_id,
        text="Your mail subscription has been cancelled and your data deleted. If you would like to resubscribe, please use the `/subscribe` command.",
    )
