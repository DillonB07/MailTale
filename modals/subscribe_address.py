def get_modal(user_id):
    return {
        "type": "modal",
        "callback_id": "subscribe_address",
        "title": {"type": "plain_text", "text": "Subscribe!", "emoji": True},
        "submit": {"type": "plain_text", "text": "Continue", "emoji": True},
        "close": {"type": "plain_text", "text": "Cancel", "emoji": True},
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"Heya <@{user_id}>, I think that email is so boring now. Let's be honest, you don't enjoy reading your emails. So, why should you? I'll send you a physical letter each month!",
                },
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "_Just to be clear, I'm doing this of my own accord and this is not endorsed by HQ._",
                    }
                ],
            },
            {"type": "divider"},
            {
                "type": "input",
                "block_id": "name",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "name",
                    "placeholder": {"type": "plain_text", "text": "Heidi Hakkuun"},
                },
                "label": {"type": "plain_text", "text": "Name", "emoji": True},
            },
            {
                "type": "input",
                "block_id": "address_line_1",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "address_line_1",
                    "placeholder": {"type": "plain_text", "text": "7 Orpheus Avenue"},
                },
                "label": {
                    "type": "plain_text",
                    "text": "Address Line 1",
                    "emoji": True,
                },
            },
            {
                "type": "input",
                "block_id": "address_line_2",
                "optional": True,
                "element": {
                    "type": "plain_text_input",
                    "action_id": "address_line_2",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Phone: +44-800-RAC-COON",
                    },
                },
                "label": {
                    "type": "plain_text",
                    "text": "Address Line 2",
                    "emoji": True,
                },
            },
            {
                "type": "input",
                "block_id": "city",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "city",
                    "placeholder": {"type": "plain_text", "text": "Little Stoke"},
                },
                "label": {"type": "plain_text", "text": "City", "emoji": True},
            },
            {
                "type": "input",
                "block_id": "county",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "county",
                    "placeholder": {"type": "plain_text", "text": "Bristol"},
                },
                "label": {"type": "plain_text", "text": "County", "emoji": True},
            },
            {
                "type": "input",
                "block_id": "postcode",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "postcode",
                    "placeholder": {"type": "plain_text", "text": "BS34 6JE"},
                },
                "label": {"type": "plain_text", "text": "Post Code", "emoji": True},
            },
            {
                "type": "input",
                "block_id": "country",
                "element": {
                    "type": "static_select",
                    "action_id": "country",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select an item",
                        "emoji": True,
                    },
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "United Kingdom",
                                "emoji": True,
                            },
                            "value": "United Kingdom",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Argentina",
                                "emoji": True,
                            },
                            "value": "Argentina",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Armenia",
                                "emoji": True,
                            },
                            "value": "Armenia",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Australia",
                                "emoji": True,
                            },
                            "value": "Australia",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Austria",
                                "emoji": True,
                            },
                            "value": "Austria",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Azerbaijan",
                                "emoji": True,
                            },
                            "value": "Azerbaijan",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Belgium",
                                "emoji": True,
                            },
                            "value": "Belgium",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Bolivia",
                                "emoji": True,
                            },
                            "value": "Bolivia",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Bosnia-Herzegovina",
                                "emoji": True,
                            },
                            "value": "Bosnia-herzegovina",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Botswana",
                                "emoji": True,
                            },
                            "value": "Botswana",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Brazil",
                                "emoji": True,
                            },
                            "value": "Brazil",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Bulgaria",
                                "emoji": True,
                            },
                            "value": "Bulgaria",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Canada",
                                "emoji": True,
                            },
                            "value": "Canada",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Cape Verde",
                                "emoji": True,
                            },
                            "value": "Cape-verde",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Central African Republic",
                                "emoji": True,
                            },
                            "value": "Central African Republic",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "China (People’s Republic)",
                                "emoji": True,
                            },
                            "value": "China",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Colombia",
                                "emoji": True,
                            },
                            "value": "Colombia",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Croatia",
                                "emoji": True,
                            },
                            "value": "Croatia",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Cuba",
                                "emoji": True,
                            },
                            "value": "Cuba",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Czech Republic",
                                "emoji": True,
                            },
                            "value": "Czech Republic",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Denmark",
                                "emoji": True,
                            },
                            "value": "Denmark",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Dominican Republic",
                                "emoji": True,
                            },
                            "value": "Dominican Republic",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Ecuador",
                                "emoji": True,
                            },
                            "value": "Ecuador",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Egypt",
                                "emoji": True,
                            },
                            "value": "Egypt",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Estonia",
                                "emoji": True,
                            },
                            "value": "Estonia",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Ethiopia",
                                "emoji": True,
                            },
                            "value": "Ethiopia",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Finland",
                                "emoji": True,
                            },
                            "value": "Finland",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "France",
                                "emoji": True,
                            },
                            "value": "France",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Georgia",
                                "emoji": True,
                            },
                            "value": "Georgia",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Germany",
                                "emoji": True,
                            },
                            "value": "Germany",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Greece",
                                "emoji": True,
                            },
                            "value": "Greece",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Hong Kong",
                                "emoji": True,
                            },
                            "value": "Hong Kong",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Hungary",
                                "emoji": True,
                            },
                            "value": "Hungary",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Iceland",
                                "emoji": True,
                            },
                            "value": "Iceland",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "India",
                                "emoji": True,
                            },
                            "value": "India",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Indonesia",
                                "emoji": True,
                            },
                            "value": "Indonesia",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Iran",
                                "emoji": True,
                            },
                            "value": "Iran",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Iraq",
                                "emoji": True,
                            },
                            "value": "Iraq",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Ireland",
                                "emoji": True,
                            },
                            "value": "Ireland",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Israel",
                                "emoji": True,
                            },
                            "value": "Israel",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Italy",
                                "emoji": True,
                            },
                            "value": "Italy",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Japan",
                                "emoji": True,
                            },
                            "value": "Japan",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Jordan",
                                "emoji": True,
                            },
                            "value": "Jordan",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Kenya",
                                "emoji": True,
                            },
                            "value": "Kenya",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Republic of (South) Korea",
                                "emoji": True,
                            },
                            "value": "Republic of Korea",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Latvia",
                                "emoji": True,
                            },
                            "value": "Latvia",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Lebanon",
                                "emoji": True,
                            },
                            "value": "Lebanon",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Lesotho",
                                "emoji": True,
                            },
                            "value": "Lesotho",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Lithuania",
                                "emoji": True,
                            },
                            "value": "Lithuania",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Luxembourg",
                                "emoji": True,
                            },
                            "value": "Luxembourg",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Macao",
                                "emoji": True,
                            },
                            "value": "Macao",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Malaysia",
                                "emoji": True,
                            },
                            "value": "Malaysia",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Malta",
                                "emoji": True,
                            },
                            "value": "Malta",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Mexico",
                                "emoji": True,
                            },
                            "value": "Mexico",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Moldova",
                                "emoji": True,
                            },
                            "value": "Moldova",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Mongolia",
                                "emoji": True,
                            },
                            "value": "Mongolia",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Morocco",
                                "emoji": True,
                            },
                            "value": "Morocco",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Mozambique",
                                "emoji": True,
                            },
                            "value": "Mozambique",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Namibia",
                                "emoji": True,
                            },
                            "value": "Namibia",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Nepal",
                                "emoji": True,
                            },
                            "value": "Nepal",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Netherlands",
                                "emoji": True,
                            },
                            "value": "Netherlands",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "New Zealand",
                                "emoji": True,
                            },
                            "value": "New Zealand",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Nicaragua",
                                "emoji": True,
                            },
                            "value": "Nicaragua",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Nigeria",
                                "emoji": True,
                            },
                            "value": "Nigeria",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Norway",
                                "emoji": True,
                            },
                            "value": "Norway",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Oman",
                                "emoji": True,
                            },
                            "value": "Oman",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Pakistan",
                                "emoji": True,
                            },
                            "value": "Pakistan",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Paraguay",
                                "emoji": True,
                            },
                            "value": "Paraguay",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Peru",
                                "emoji": True,
                            },
                            "value": "Peru",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Philippines",
                                "emoji": True,
                            },
                            "value": "Philippines",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Poland",
                                "emoji": True,
                            },
                            "value": "Poland",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Portugal",
                                "emoji": True,
                            },
                            "value": "Portugal",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Qatar",
                                "emoji": True,
                            },
                            "value": "Qatar",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Romania",
                                "emoji": True,
                            },
                            "value": "Romania",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Russia",
                                "emoji": True,
                            },
                            "value": "Russia",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Rwanda",
                                "emoji": True,
                            },
                            "value": "Rwanda",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Saudi Arabia",
                                "emoji": True,
                            },
                            "value": "Saudi Arabia",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Senegal",
                                "emoji": True,
                            },
                            "value": "Senegal",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Singapore",
                                "emoji": True,
                            },
                            "value": "Singapore",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Slovakia",
                                "emoji": True,
                            },
                            "value": "Slovakia",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Slovenia",
                                "emoji": True,
                            },
                            "value": "Slovenia",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "South Africa",
                                "emoji": True,
                            },
                            "value": "South Africa",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Spain",
                                "emoji": True,
                            },
                            "value": "Spain",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Sudan",
                                "emoji": True,
                            },
                            "value": "Sudan",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Sweden",
                                "emoji": True,
                            },
                            "value": "Sweden",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Switzerland",
                                "emoji": True,
                            },
                            "value": "Switzerland",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Tajikistan",
                                "emoji": True,
                            },
                            "value": "Tajikistan",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Tanzania",
                                "emoji": True,
                            },
                            "value": "Tanzania",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Thailand",
                                "emoji": True,
                            },
                            "value": "Thailand",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Turkey",
                                "emoji": True,
                            },
                            "value": "Turkey",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Turkmenistan",
                                "emoji": True,
                            },
                            "value": "Turkmenistan",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "United States of America",
                                "emoji": True,
                            },
                            "value": "United States",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Uganda",
                                "emoji": True,
                            },
                            "value": "Uganda",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Ukraine",
                                "emoji": True,
                            },
                            "value": "Ukraine",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "United Arab Emirates",
                                "emoji": True,
                            },
                            "value": "United Arab Emirates",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Uruguay",
                                "emoji": True,
                            },
                            "value": "Uruguay",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Uzbekistan",
                                "emoji": True,
                            },
                            "value": "Uzbekistan",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Vanuatu",
                                "emoji": True,
                            },
                            "value": "Vanuatu",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Vietnam",
                                "emoji": True,
                            },
                            "value": "Vietnam",
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Zimbabwe",
                                "emoji": True,
                            },
                            "value": "Zimbabwe",
                        },
                    ],
                },
                "label": {"type": "plain_text", "text": "Country", "emoji": True},
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "_If your country isn't here, send <@U054VC2KM9P> a DM asking about it. The full list of countries we can ship to is <https://www.royalmail.com/sending/international/country-guides|here>._",
                    }
                ],
            },
        ],
    }
