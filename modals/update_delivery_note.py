from utils.airtable import airtable

def get_modal(user_id):
    user = airtable.get_user(user_id)
    if not user: return
    delivery_note = user["fields"].get("Delivery Notes", "")
    
    return {
	"title": {
		"type": "plain_text",
		"text": "Manage Subscription",
		"emoji": True
	},
    "callback_id": "update_delivery_note",
	"type": "modal",
	"close": {
		"type": "plain_text",
		"text": "Cancel",
		"emoji": True
	},
	"submit": {
		"type": "plain_text",
		"text": "Update",
		"emoji": True
	},
	"blocks": [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Update Delivery Note",
				"emoji": True
			}
		},
		{
			"type": "input",
            "block_id": "delivery-note",
			"element": {
				"type": "plain_text_input",
				"multiline": True,
				"action_id": "delivery-note",
                "initial_value": delivery_note
			},
			"label": {
				"type": "plain_text",
				"text": "Label",
				"emoji": True
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "plain_text",
					"text": "These notes will be passed to the Hack Clubber mailing to you",
					"emoji": True
				}
			]
		}
	]
}