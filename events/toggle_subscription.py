from utils.env import env


def handle_toggle_subscription(body, client):
    user_id = body["user"]["id"]
    user = env.airtable.get_user(user_id)
    if not user:
        return

    paused = user["fields"].get("Paused", False)
    env.airtable.update_user(user_id, **{"Paused": not paused})

    client.chat_postMessage(
        channel=user_id,
        text=(
            "Your mail subscription has been paused!"
            if not paused
            else "Your mail subscription has been resumed!"
        ),
    )
