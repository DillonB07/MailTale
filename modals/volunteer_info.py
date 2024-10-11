from utils.airtable import airtable

def get_modal(user_id):
    user = airtable.get_user(user_id)
    if not user: return
    subscribers = airtable.get_users()
    if not subscribers: return
    total_signups = len(subscribers)
    total_countries = len(set([subscriber["fields"]["Country"] for subscriber in subscribers]))
    
    return {
            "title": {
                "type": "plain_text",
                "text": "Manage Subscription",
                "emoji": True
            },
            "callback_id": "volunteer_info",
            "type": "modal",
            "close": {
                "type": "plain_text",
                "text": "Cancel",
                "emoji": True
            },
            "submit": {
                "type": "plain_text",
                "text": "Next",
                "emoji": True
            },
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"Currently, {total_signups} hackers have signed up for the newsletter from {total_countries} different countries! Wow, that's a *lot* of letters to handwrite and mail out.",
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Instead of painfully writing everything myself and breaking my wrists, what if there was a team mailing them out? If you're still here, I'm guessing you're interested in helping out! Here's what it would involve:"
                    }    
                },
                {
			"type": "rich_text",
			"elements": [
				{
					"type": "rich_text_list",
					"style": "bullet",
					"elements": [
						{
							"type": "rich_text_section",
							"elements": [
								{
									"type": "text",
									"text": "Handwriting 10 or less newsletters per month"
								},
							]
						},
						{
							"type": "rich_text_section",
							"elements": [
								{
									"type": "text",
									"text": "Mailing those letters to Hackers all over the globe!"
								},
							]
						},
                        {
							"type": "rich_text_section",
                            "elements": [
                                {
                                	"type": "text",
	                            	"text": "Being spoilt on the month's newsletter :("
                                }
							]
						},
                        {
							"type": "rich_text_section",
                            "elements": [
                                {
                                	"type": "text",
	                            	"text": "Getting to use the mail system (one of the best systems in the world!)"
                                }
							]
						},
                        {
							"type": "rich_text_section",
                            "elements": [
                                {
                                	"type": "text",
	                            	"text": "Contributing to the newsletter"
                                }
							]
						},
                        {
							"type": "rich_text_section",
                            "elements": [
                                {
                                	"type": "text",
	                            	"text": "But most importantly, making Hackers happy!"
                                }
							]
						}
					]
				}
			]
		}
            ]
    }