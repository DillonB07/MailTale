from utils.airtable import airtable

def get_modal(user_id):
	user = airtable.get_user(user_id)
	if not user: return
	paused = user["fields"].get("Paused", False)

	return {
		"type": "modal",
		"callback_id": "manage_subscription",
		"title": {
			"type": "plain_text",
			"text": "Manage Subscription",
			"emoji": True
		},
		"close": {
			"type": "plain_text",
			"text": "Close",
			"emoji": True
		},
		"blocks": [
			{
				"type": "header",
				"text": {
					"type": "plain_text",
					"text": "Your newsletter subscription is :sparkles: active :sparkles: :roo-yay:" if not paused else "Your newsletter subscription is :no_entry_sign: paused :no_entry_sign: :roo-sad:",
					"emoji": True
				}
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": f"Welcome to the mail management dashboard <@{user_id}>!\nPlease choose an option below.",
				}
			},
			{
				"type": "actions",
				"block_id": "manage-address",
				"elements": [
					{
						"type": "button",
						"text": {
							"type": "plain_text",
							"text": "Manage Address",
							"emoji": True
						},
						"value": "manage-address",
						"action_id": "manage-address"
					}
				]
			},
			{
				"type": "actions",
				"block_id": "manage-status",
				"elements": [
					{
						"type": "button",
						"text": {
							"type": "plain_text",
							"text": "Manage Status",
							"emoji": True
						},
						"value": "manage-status",
						"action_id": "manage-status"
					}
				]
			},
			{
				"type": "actions",
				"block_id": "volunteer-info",
				"elements": [
					{
						"type": "button",
						"text": {
							"type": "plain_text",
							"text": "Manage Volunteering",
							"emoji": True
						},
						"value": "volunteer-info",
						"action_id": "volunteer-info"
					}
				]
			}
		]
	}