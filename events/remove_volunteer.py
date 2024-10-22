from utils.env import env


def handle_remove_volunteer(body, client):
    user_id = body["user"]["id"]
    env.airtable.update_user(user_id, **{"Wants to Mail": False})
    client.chat_postMessage(
        channel=user_id,
        text="You have been removed from the volunteer list. If you'd like to sign up to volunteer at any point in the future, you can do so through the `/subscription` menu",
    )
