Facebook-link-extracter Version 1.0 1/10/2020


This Python program extracts links from a Facebook chat and writes them to a Google sheet. 

rickywolff@gmail.com

## Dependencies

This program requires two Python libraries: 

1. [fbchat](https://github.com/carpedm20/fbchat): Python module for interfacing with Facebook messenger. `pip install fbchat`.

2. [pygsheets](https://github.com/nithinmurali/pygsheets): Python module for interfacing with Google sheets. `pip install pygsheets`.

* To use pygsheets, obtain OAuth2 credentials from Google Developers Console for google spreadsheet api and drive api and save the file as client_secret.json in same directory as project. [read more here](https://pygsheets.readthedocs.io/en/latest/authorization.html).

## Usage
0. Install dependencies and obtain OAuth2 credentials.
1. Open fb_links_settings.py and set variables as directed.
2. Run create_link_sheet.py to scrape your chat for all previously posted links. (E.g.: `python3 /Users/richardwolff/create_link_sheet.py`).
3. Schedule update_link_sheet.py to run as a cron job, keeping your sheet updated. (E.g. add `0 */6 * * * python3 /Users/richardwolff/update_link_sheet.py` to cron using `crontab -e` to update every six hours).
