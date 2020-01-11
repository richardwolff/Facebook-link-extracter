Facebook-link-extracter Version 1.0 1/10/2020


This program extracts links from a Facebook chat and writes them to a Google sheet. 

rickywolff@gmail.com

## Dependencies

1. [fbchat](https://github.com/carpedm20/fbchat): python module for interfacing with Facebook messenger

`pip install fbchat`

2. [pygsheets](https://github.com/nithinmurali/pygsheets): python module for interfacing with Google sheets

`pip install pygsheets`

To use pygsheets, obtain OAuth2 credentials from Google Developers Console for google spreadsheet api and drive api and save the file as client_secret.json in same directory as project. [read more here](https://pygsheets.readthedocs.io/en/latest/authorization.html).

## Basic usage

1. Run create_link_sheet.py to scrape your chat for all previously posted links. 
2. Schedule update_link_sheet.py to run as a cron job, keeping your sheet updated. 
