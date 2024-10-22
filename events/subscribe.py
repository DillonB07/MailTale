from utils.env import env


def handle_subscribe_address(body, client):
    user_id = body["user"]["id"]

    view = body["view"]
    data = view["state"]["values"]

    name = data["name"]["name"]["value"]
    raw_address = data["address"]["address"]["value"]
    country = data["country"]["country"]["selected_option"]["value"]

    env.airtable.create_user(
        user_id=user_id,
        name=name,
        raw_address=raw_address,
        country=country,
    )

    client.chat_postMessage(
        channel=user_id,
        user=user_id,
        text="Thanks for subscribing to the newsletter!",
    )

    client.chat_postMessage(
        channel=env.slack_public_channel,
        text=f":blob_bounce: Somebody has subscribed to the newsletter from {country}!! :yay:",
    )

    client.chat_postMessage(
        channel=env.slack_mailroom_channel,
        text=f":blob_bounce: <@{user_id}> just subscribed from {country}!",
    )
